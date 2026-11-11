#!/usr/bin/env python3
"""Validate the companion language patch and quest script."""

from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LANG = ROOT / "src/main/resources/assets/epicclassmod/lang/es_es.json"
QUESTS = ROOT / "src/main/resources/assets/epicclassmod/quests/es_es.txt"
ENGLISH_PATH = "assets/epicclassmod/lang/en_us.json"
SPANISH_PATH = "assets/epicclassmod/lang/es_es.json"
PLACEHOLDER = re.compile(r"%(?:\d+\$)?[sdif]")


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Clave JSON duplicada: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=no_duplicate_keys,
    )


def check_against_original_jar(jar_path, translations):
    with zipfile.ZipFile(jar_path) as jar:
        english = json.loads(jar.read(ENGLISH_PATH).decode("utf-8"))
        original_spanish = json.loads(jar.read(SPANISH_PATH).decode("utf-8"))

    unknown = sorted(set(translations) - set(english))
    if unknown:
        raise ValueError(
            "Claves que no existen en el archivo inglés original: "
            + ", ".join(unknown[:12])
        )

    missing = set(english) - set(original_spanish) - set(translations)
    if missing:
        raise ValueError(
            f"Quedan {len(missing)} claves sin traducción. "
            f"Ejemplos: {', '.join(sorted(missing)[:12])}"
        )

    mismatched = []
    for key, translated in translations.items():
        source_placeholders = Counter(PLACEHOLDER.findall(english[key]))
        translated_placeholders = Counter(PLACEHOLDER.findall(translated))
        if source_placeholders != translated_placeholders:
            mismatched.append(key)
    if mismatched:
        raise ValueError(
            "Los marcadores de formato no coinciden en: "
            + ", ".join(mismatched[:12])
        )

    print(
        f"OK: las {len(translations)} claves del complemento existen en el mod "
        f"y, junto con {len(original_spanish)} claves originales, cubren "
        f"las {len(english)} claves inglesas."
    )
    print("OK: los marcadores de formato coinciden con el texto inglés.")


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--original-jar",
        help="Ruta al JAR original Epic Class Mod 3.0.2 para validar claves y marcadores.",
    )
    args = parser.parse_args()

    translations = read_json(LANG)
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

    if args.original_jar:
        check_against_original_jar(args.original_jar, translations)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"Error al validar recursos: {exc}", file=sys.stderr)
        raise SystemExit(1)
