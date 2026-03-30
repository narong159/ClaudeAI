import json
import helpers_upgrade

def generate_report(filename="report.html"):
    rows = ""
    for test in helpers_upgrade.results:
        row_color = "#ffcccc" if test['result'] == "❌ Fail" else ""
        rows += f"""
        <tr style="background-color: {row_color};">
            <td>{test['case_id']}</td>
            <td>{test['method']}</td>
            <td>{test['url']}</td>
            <td><pre>{json.dumps(test['request'], indent = 2)}</pre></td>
            <td>{test['status_code']}</td>
            <td>{test['response_time']}</td>
            <td><pre>{json.dumps(test['response'], indent = 2)}</pre></td>
            <td>{test['expected']}</td>
            <td>{test['actual']}</td>
            <td>{test['result']}</td>
        </tr>
        """

    total = len(helpers_upgrade.results)
    passed = sum(1 for t in helpers_upgrade.results if t['result'] == "✅ Pass")
    failed = total - passed
    html = f"""
    <html>
        <head>
            <title>API Test Report</title>
            <style>
                body {{ font-family: Arial; padding: 20px; }}
                table {{ border-collapse: collapse; width: 100%; table-layout: fixed; }}
                th {{ background-color: #4CAF50; color: white; padding: 10px; }}
                td {{ border: 1px solid #ddd; padding: 8px; vertical-align: top; }}
                tr:nth-child(even) {{ background-color: #f2f2f2; }}
                pre {{  margin: 0; font-size: 12px; white-space: pre-wrap; word-break: break-all;}}
                th:nth-child(1), td:nth-child(1) {{ width: 40px; }}
                th:nth-child(2), td:nth-child(2) {{ width: 60px; }}
                th:nth-child(3), td:nth-child(3) {{ width: 200px; word-break: break-all; }}
                th:nth-child(4), td:nth-child(4) {{ width: 250px; }}
                th:nth-child(5), td:nth-child(5) {{ width: 40px; }}
                th:nth-child(6), td:nth-child(6) {{ width: 40px; }}
                th:nth-child(7), td:nth-child(7) {{ width: 400px; }}
                th:nth-child(8), td:nth-child(8) {{ width: 80px; }}
                th:nth-child(9), td:nth-child(9) {{ width: 80px; }}
                th:nth-child(10), td:nth-child(10) {{ width: 60px; }}
            </style>
        </head>
        <body>
            <h2>API Test Report</h2>
            <div style="margin-bottom: 20px;">
                <span style="background:#4CAF50; color:white; padding:8px 15px; border-radius:5px; margin-right:10px;">
                    Total: {total}
                </span>
                <span style="background:#2196F3; color:white; padding:8px 15px; border-radius:5px; margin-right:10px;">
                    ✅ Passed: {passed}
                </span>
                <span style="background:#f44336; color:white; padding:8px 15px; border-radius:5px;">
                    ❌ Failed: {failed}
                </span>
            </div>
            <table>
                <tr>
                    <th>CaseID</th>
                    <th>Method</th>
                    <th>URL</th>
                    <th>Request</th>
                    <th>Status</th>
                    <th>Time</th>
                    <th>Response</th>
                    <th>Expected</th>
                    <th>Actual</th>
                    <th>Result</th>
                </tr>
                {rows}
            </table>
        </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Report generated: {filename}")    