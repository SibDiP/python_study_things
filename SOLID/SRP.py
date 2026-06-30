# Original God Obj
class ReportManager:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        # Сложная логика генерации отчета
        report = f"Report based on {self.data}"
        return report

    def save_report_to_file(self, report, filename):
        with open(filename, 'w') as f:
            f.write(report)

    def send_report_via_email(self, report, email_address):
        print(f"Sending report to {email_address}: {report}")

# SRP refactoring

from dataclasses import dataclass

@dataclass
class ReportData:
        content: str
    
class ReportGenerator:
    def generate(self, raw_data: str) -> ReportData:
        formatted_report = f"Report based on {raw_data}"
        return ReportData(content=formatted_report)

class FileManager:
    @staticmethod
    def save_to_file(report: ReportData, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(report.content)

class MailManager:
    @staticmethod
    def sent_report_via_email(report: ReportData, email_address: str) -> None:
        print(f"Sending report to {email_address}: {report.content}")
