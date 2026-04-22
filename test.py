from main import process_string

test_cases = {
    "hello": "hElLo",
    "123456": "123456",
    "github": "gItHuB"
}

html = "<html><body style='font-family: Arial;'><h2 style='color: #2c3e50;'>Test Report (Variant 4)</h2>"
html += "<table border='1' cellpadding='8' style='border-collapse: collapse; text-align: center;'>"
html += "<tr style='background-color: #3498db; color: white;'><th>Input</th><th>Expected</th><th>Output</th><th>Test Status</th></tr>"

for inp, expected in test_cases.items():
    result = process_string(inp)
    status = "Passed" if result == expected else "Failed"
    color = "#2ecc71" if status == "Passed" else "#e74c3c"
    html += f"<tr><td>{inp}</td><td>{expected}</td><td>{result}</td><td style='background-color:{color}; color:white; font-weight:bold;'>{status}</td></tr>"

html += "</table></body></html>"

with open("report.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Testing complete. HTML Report generated.")
