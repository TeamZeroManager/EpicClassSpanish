#!/usr/bin/env python3
"""Validate the companion's language and main-quest resources."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LANG = ROOT / "src/main/resources/assets/epicclassmod/lang/es_es.json"
QUESTS = ROOT / "src/main/resources/assets/epicclassmod/quests/es_es.txt"


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Clave JSON duplicada: {key}")
        result[key] = value
    return result


def main():
    translations = json.loads(
        LANG.read_text(encoding="utf-8"),
        object_pairs_hook=no_duplicate_keys,
    )
    if not translations:
        raise SystemExit("El parche de idioma está vacío.")
    if not all(isinstance(k, str) and isinstance(v, str)
               for k, v in translations.items()):
        raise SystemExit("Todas las claves y traducciones deben ser texto.")

    quest_text = QUESTS.read_text(encoding="utf-8")
    headers = re.findall(r"^===\s+(.+)$", quest_text, flags=re.MULTILINE)
    numbered = [h for h in headers if re.match(r"\d+\s*[·.]\s*", h)]
    epilogues = [h for h in headers if h.lower().startswith("end")]

    if len(numbered) != 23:
        raise SystemExit(
            f"Se esperaban 23 misiones principales; se encontraron {len(numbered)}."
        )
    if len(epilogues) != 1:
        raise SystemExit(
            f"Se esperaba un epílogo; se encontraron {len(epilogues)}."
        )

    print(f"OK: {len(translations)} claves de idioma válidas.")
    print("OK: 23 misiones principales y un epílogo.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Error al validar recursos: {exc}", file=sys.stderr)
        raise SystemExit(1)
