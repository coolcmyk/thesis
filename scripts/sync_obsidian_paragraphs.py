#!/usr/bin/env python3
"""Generate Obsidian paragraph notes from the canonical Bab I--II LaTeX source.

Paragraphs marked with ``% [SRC-B1-01]`` or ``% [SRC-B2-01]`` are extracted
from their .tex files. Do not edit generated files in obsidian/Paragraphs/;
edit the corresponding LaTeX paragraph and run this script instead.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NOTES: dict[str, tuple[str, str, list[str]]] = {
    "SRC-B1-01": ("B1-01 - Keputusan dan lintasan UAV", "Bab I", ["Papers/Vivaldini 2025 - Decision-Making-Based Path Planning for Autonomous UAVs"]),
    "SRC-B1-02": ("B1-02 - Navigasi tujuan objek UAV", "Bab I", ["Papers/Ayala 2024 - UAV Object-Goal Navigation Review"]),
    "SRC-B1-03": ("B1-03 - Grounding dan kemajuan instruksi", "Bab I", ["Papers/Zhang Kordjamshidi 2022 - Explicit Object Relation Alignment", "Papers/Ma 2019 - Self-Monitoring Navigation Agent"]),
    "SRC-B1-04": ("B1-04 - Dasar VLM", "Bab I", ["Papers/Radford 2021 - CLIP", "Papers/Vinyals 2015 - Show and Tell"]),
    "SRC-B1-05": ("B1-05 - ROS 2 dan integrasi", "Bab I", ["Papers/Shah et al 2017 - AirSim", "Papers/Jansen et al 2023 - CoSyS-AirSim", "Papers/Macenski 2022 - ROS 2"]),
    "SRC-B1-06": ("B1-06 - Benchmark UAV", "Bab I", ["Papers/Zhang et al 2025 - VLM Sky-Ready"]),
    "SRC-B2-01": ("B2-01 - UAV dan navigasi otonom", "Bab II", ["Papers/Vivaldini 2025 - Decision-Making-Based Path Planning for Autonomous UAVs", "Papers/Ayala 2024 - UAV Object-Goal Navigation Review"]),
    "SRC-B2-02": ("B2-02 - Navigasi geometris dan semantik", "Bab II", ["Papers/Ayala 2024 - UAV Object-Goal Navigation Review"]),
    "SRC-B2-03": ("B2-03 - Model visi bahasa", "Bab II", ["Papers/Radford 2021 - CLIP", "Papers/Vinyals 2015 - Show and Tell"]),
    "SRC-B2-04": ("B2-04 - Penalaran spasial", "Bab II", ["Papers/Zhang Kordjamshidi 2022 - Explicit Object Relation Alignment"]),
    "SRC-B2-05": ("B2-05 - Instruksi multilangkah", "Bab II", ["Papers/Ma 2019 - Self-Monitoring Navigation Agent"]),
    "SRC-B2-06": ("B2-06 - ROS 2 dan frame", "Bab II", ["Papers/Macenski 2022 - ROS 2"]),
    "SRC-B2-07": ("B2-07 - Benchmark reproduksibel", "Bab II", ["Papers/Zhang et al 2025 - VLM Sky-Ready"]),
    "SRC-B2-08": ("B2-08 - VLM untuk inspeksi UAV", "Bab II", ["Papers/Radford 2021 - CLIP", "Papers/Vinyals 2015 - Show and Tell", "Papers/van der Wal 2026 - VLM Guided UAV Inspection"]),
    "SRC-B2-09": ("B2-09 - Navigasi UAV berbasis bahasa", "Bab II", ["Papers/Zhang Kordjamshidi 2022 - Explicit Object Relation Alignment", "Papers/Ma 2019 - Self-Monitoring Navigation Agent", "Papers/Ayala 2024 - UAV Object-Goal Navigation Review", "Papers/Zhang et al 2025 - VLM Sky-Ready"]),
    "SRC-B2-10": ("B2-10 - LoRA dan QLoRA", "Bab II", ["Papers/Hu et al 2021 - LoRA", "Papers/Dettmers et al 2023 - QLoRA"]),
    "SRC-B2-11": ("B2-11 - GRPO untuk VLM", "Bab II", ["Papers/Shao et al 2024 - DeepSeekMath", "Papers/Huang et al 2025 - Vision-R1", "Papers/Shen et al 2025 - VLM-R1"]),
    "SRC-B2-12": ("B2-12 - AirSim dan CoSyS-AirSim", "Bab II", ["Papers/Shah et al 2017 - AirSim", "Papers/Jansen et al 2023 - CoSyS-AirSim"]),
}

MARKER = re.compile(r"% \[(SRC-B[12]-\d{2})\]")
CITATION = re.compile(r"\\cite\w*\{[^}]*\}")


def extract_marked_paragraphs(tex_path: Path) -> dict[str, str]:
    """Return raw LaTeX paragraphs immediately preceding each source marker."""
    text = tex_path.read_text(encoding="utf-8")
    paragraphs: dict[str, str] = {}
    for match in MARKER.finditer(text):
        marker = match.group(1)
        before = text[: match.start()]
        start = before.rfind("\n\n") + 2
        lines = before[start:].strip().splitlines()
        # The first source paragraph in a section follows section comments and
        # a label; those structural lines are not part of the prose note.
        while lines and (
            lines[0].lstrip().startswith("%")
            or lines[0].lstrip().startswith("\\section")
            or lines[0].lstrip().startswith("\\label")
        ):
            lines.pop(0)
        paragraph = "\n".join(lines).strip()
        if not paragraph:
            raise ValueError(f"No paragraph found before {marker} in {tex_path}")
        paragraphs[marker] = paragraph
    return paragraphs


def latex_to_markdown(text: str) -> str:
    """Convert the small LaTeX subset used in prose into readable Markdown."""
    text = CITATION.sub("", text)
    text = re.sub(r"\\textit\{([^{}]*)\}", r"*\1*", text)
    text = re.sub(r"\\texttt\{([^{}]*)\}", r"`\1`", text)
    text = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", text)
    text = text.replace(r"\_", "_")
    text = text.replace(r"\%", "%")
    text = text.replace("~", " ")
    text = text.replace("--", "—")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    return text


def make_note(marker: str, latex: str) -> tuple[Path, str]:
    filename, chapter, papers = NOTES[marker]
    chapter_file = "01-bab1.tex" if marker.startswith("SRC-B1") else "02-bab2.tex"
    links = "; ".join(f"[[{paper}]]" for paper in papers)
    markdown = latex_to_markdown(latex)
    content = (
        "<!-- GENERATED by scripts/sync_obsidian_paragraphs.py; edit the .tex source, not this file. -->\n"
        f"# {filename}\n\n"
        f"{markdown}\n\n"
        f"**Sumber:** {links}<br>\n"
        f"**Naskah:** `src/01-body/{chapter_file}`, `{marker}`\n"
    )
    return ROOT / "obsidian" / "Paragraphs" / f"{filename}.md", content


def main() -> None:
    paragraphs = {}
    paragraphs.update(extract_marked_paragraphs(ROOT / "src/01-body/01-bab1.tex"))
    paragraphs.update(extract_marked_paragraphs(ROOT / "src/01-body/02-bab2.tex"))

    expected = set(NOTES)
    found = set(paragraphs)
    missing = expected - found
    unknown = found - expected
    if missing or unknown:
        raise SystemExit(f"Source-marker mismatch; missing={sorted(missing)}, unknown={sorted(unknown)}")

    for marker in sorted(NOTES):
        output, content = make_note(marker, paragraphs[marker])
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")
    print(f"Synced {len(NOTES)} Obsidian paragraph notes from LaTeX.")


if __name__ == "__main__":
    main()
