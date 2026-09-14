#!/usr/bin/env python3
"""Deterministic contract checks for the board-cy template.

The board-cy Skill is a methodology template, not a board instance.  This test
verifies the template structure that every instance builds on:

- SKILL.md has a valid YAML frontmatter with ``name: board-cy`` and a
  ``description``.
- The board-contract JSON schema exists and is itself valid JSON.
- The schema exposes the fields the checker script depends on
  (boot0, peripheral_power(+active_level), usb_dn/usb_dp, aliases, keys).
- INSTANCE-GUIDE.md exists (the instantiation path).
- The checker script exists and is runnable.

Board instances additionally provide a ``board-contract.json`` and per-board
references; those are validated per instance, not by this template test.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
SCHEMA = json.loads(
    (ROOT / "references" / "board-contract.schema.json").read_text(encoding="utf-8")
)
CHECKER = ROOT / "scripts" / "check_board_baseline.py"


def require(text: str) -> None:
    if text not in SKILL:
        raise AssertionError(f"missing skill contract: {text}")


def main() -> None:
    # --- SKILL.md frontmatter ----------------------------------------------
    match = re.match(r"\A---\n(.*?)\n---\n", SKILL, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing YAML frontmatter in SKILL.md")
    frontmatter = match.group(1)
    if "name: board-cy" not in frontmatter:
        raise AssertionError("wrong skill name in frontmatter")
    if "description:" not in frontmatter:
        raise AssertionError("missing description in frontmatter")
    if "## 新板实例化" not in SKILL:
        raise AssertionError("SKILL.md must contain the instantiation section")
    if "INSTANCE-GUIDE.md" not in SKILL:
        raise AssertionError("SKILL.md instantiation section must reference INSTANCE-GUIDE.md")

    # --- required top-level sections ---------------------------------------
    for section in (
        "模板与实例的关系",
        "定位",
        "先执行这套上下文工作流",
        "板的不可破坏合同",
        "事实冲突处理",
        "项目边界",
        "完成标准",
        "禁止事项",
        "新板实例化",
    ):
        require(f"## {section}")

    # --- schema validity ----------------------------------------------------
    if SCHEMA.get("$schema") != "http://json-schema.org/draft-07/schema#":
        raise AssertionError("board-contract.schema.json must be draft-07")
    if SCHEMA.get("title") != "board-cy board-contract.json":
        raise AssertionError("wrong schema title")

    required_root = SCHEMA.get("required", [])
    for field in ("schema_version", "contract_id", "scope", "verified_at", "aliases", "soc", "pins"):
        if field not in required_root:
            raise AssertionError(f"schema missing required root field: {field}")

    # --- checker dependencies are present in the schema ----------------------
    boot = SCHEMA.get("properties", {}).get("boot", {})
    if "gpio" not in boot.get("properties", {}):
        raise AssertionError("schema boot section must expose gpio (boot0)")
    usb = SCHEMA.get("properties", {}).get("usb", {})
    usb_props = usb.get("properties", {})
    if "dn_gpio" not in usb_props or "dp_gpio" not in usb_props:
        raise AssertionError("schema usb section must expose dn_gpio/dp_gpio")
    power = SCHEMA.get("properties", {}).get("power", {})
    power_props = power.get("properties", {})
    if "gpio" not in power_props or "active_level" not in power_props:
        raise AssertionError("schema power section must expose gpio/active_level")
    pins = SCHEMA.get("properties", {}).get("pins", {})
    if "patternProperties" not in pins:
        raise AssertionError("schema pins section must be an open key->fact map")
    aliases = SCHEMA.get("properties", {}).get("aliases", {})
    if aliases.get("required") != ["product"]:
        raise AssertionError("schema aliases section must require product")

    # --- instance guide exists ----------------------------------------------
    guide = ROOT / "references" / "INSTANCE-GUIDE.md"
    if not guide.is_file():
        raise AssertionError("missing references/INSTANCE-GUIDE.md")
    guide_text = guide.read_text(encoding="utf-8")
    for marker in ("board-contract.json", "check_board_baseline.py", "board-contract.schema.json"):
        if marker not in guide_text:
            raise AssertionError(f"INSTANCE-GUIDE must reference {marker}")

    # --- checker runs --------------------------------------------------------
    if not CHECKER.is_file():
        raise AssertionError("missing scripts/check_board_baseline.py")
    result = subprocess.run(
        [sys.executable, str(CHECKER), "--help"],
        check=False,
        capture_output=True,
        text=True,
        timeout=5,
    )
    if result.returncode != 0:
        raise AssertionError("check_board_baseline.py --help failed")
    if "--contract" not in result.stdout:
        raise AssertionError("checker --help must advertise --contract")


if __name__ == "__main__":
    main()
    print("template contract OK")
