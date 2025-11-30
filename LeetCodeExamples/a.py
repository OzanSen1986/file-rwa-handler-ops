from pathlib import Path

front_name = Path('LeetCodeExamples')
back_name = Path('LeetCode06.py')

full_name = front_name / back_name


try:
    if full_name.exists():
        print(f'File exists: {full_name.absolute()}')
except FileNotFoundError as e:
    print(f"File Not Found: {e}")
finally:
    print(f'Process completed:-->')

















