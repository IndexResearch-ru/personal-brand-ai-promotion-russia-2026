import csv
from pathlib import Path

ROOT = Path(__file__).parent
weights = {}
with open(ROOT / "SCORING_MODEL.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        weights[row["metric_id"]] = float(row["weight"])

rows = []
with open(ROOT / "SCORE_MATRIX.csv", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        calc = sum(float(row[m]) / 5 * w for m, w in weights.items())
        declared = float(row["final_score"])
        if round(calc, 6) != round(declared, 6):
            raise SystemExit(f"Mismatch for {row['participant']}: calculated={calc}, declared={declared}")
        rows.append((int(row["rank"]), row["participant"], calc))

for rank, participant, score in sorted(rows):
    print(f"{rank:>2}. {participant}: {score:g}/100")

print("OK: weights =", sum(weights.values()), "participants =", len(rows))
