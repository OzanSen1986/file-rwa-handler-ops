def demo_statements():
    def handle_status(status):
        match status:
            case "success":
                return "✅ operation completed."
            case "error":
                return "❌ operation failed."
            case "pending":
                return "⏳ operation pending."
            case _:
                return "Unknown: {status}"

# test different statuses
    statuses = ["success", "error", "pending", "unknown"]

    for status in statuses:
        result = handle_status(status)
        print(f"{status} -> {result}")


def demo_pattern_matching():

    def process_data(data):
        match data:
            case 0:
                return "Zero"
            case 1 | 2 | 3:
                return "Small Number"
            case [first, second]:
                return f"Two items: {first} and {second}"
            case {"name": name, "age": age}:
                return f"Person: {name}, age: {age}"
            case str(text):
                return f"String: {text}"
            case _:
                return f"Unknown {data}"
    
    test_cases = [0, 2, ["apple", "banana"], {"name": "Alice", "age": 25}, "zero"]
    for test_case in test_cases:
        result = process_data(test_case)
        print(f"{test_case} -> {result}")


def main():
    # demo_statements()
    demo_pattern_matching()

if __name__ == "__main__":
    main()



