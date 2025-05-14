import re

class IntakeBot:
    def __init__(self):
        self.context = {
            "step": 0,
            "answered_fields": {}
        }

        self.fields = [
            {
                "name": "annual_income",
                "prompt": "What is your annual income?",
                "validate": lambda x, ctx: x.replace('.', '', 1).isdigit() and 0 <= float(x) <= 10_000_000,
                "error": "Please enter a valid number between 0 and 10,000,000.",
                "process": lambda x: float(x)
            },
            {
                "name": "has_liabilities",
                "prompt": "Any existing liabilities? (yes/no)",
                "validate": lambda x, ctx: x in ["yes", "no"],
                "error": "Please answer 'yes' or 'no'.",
                "process": lambda x: x
            },
            {
                "name": "liability_amount",
                "prompt": "Please enter your liability amount (minimum ₹1):",
                "validate": lambda x, ctx: x.replace('.', '', 1).isdigit() and float(x) >= 1,
                "error": "Please enter a valid number ≥ 1.",
                "process": lambda x: float(x),
                "condition": lambda ctx: ctx.get("has_liabilities") == "yes"
            },
            {
                "name": "loan_amount",
                "prompt": "What loan amount are you requesting?",
                "validate": lambda x, ctx: (
                    x.replace('.', '', 1).isdigit() and 
                    float(x) >= 1 and 
                    float(x) <= ctx.get("annual_income", 0) * 0.5
                ),
                "error": lambda ctx: f"Loan amount must be between ₹1 and ₹{ctx.get('annual_income', 0) * 0.5:.0f}.",
                "process": lambda x: float(x)
            },
            {
                "name": "dependents",
                "prompt": "How many dependents do you have? (0–10)",
                "validate": lambda x, ctx: x.isdigit() and 0 <= int(x) <= 10,
                "error": "Please enter an integer between 0 and 10.",
                "process": lambda x: int(x)
            },
            {
                "name": "email",
                "prompt": "Please enter your email address:",
                "validate": lambda x, ctx: re.match(r"^[a-zA-Z0-9._%+-]+@(gmail|yahoo|outlook)\.com$", x),
                "error": "Please enter a valid email address (e.g., name@gmail.com).",
                "process": lambda x: x
            }
        ]

    def start(self):
        print("Bot: Welcome to the intake process!\n")

        while self.context["step"] < len(self.fields):
            field = self.fields[self.context["step"]]
            name = field["name"]

            # Check if we should skip this field due to condition
            if "condition" in field and not field["condition"](self.context):
                self.context["step"] += 1
                continue

            # If already answered, skip
            if name in self.context["answered_fields"]:
                self.context["step"] += 1
                continue

            # Prompt and validate
            while True:
                print(f"Bot: {field['prompt']}")
                user_input = input("User: ").strip().lower()
                try:
                    if field["validate"](user_input, self.context):
                        value = field["process"](user_input)
                        self.context[name] = value
                        self.context["answered_fields"][name] = True
                        self.context["step"] += 1
                        break
                    else:
                        raise ValueError
                except Exception:
                    error = field["error"]
                    print(f"Bot: {error(self.context) if callable(error) else error}")

        print("\nBot: All data collected successfully:")
        print(self._format_context())

    def _format_context(self):
        return "\n".join(
            f"{k}: {v}" for k, v in self.context.items()
            if k not in ("step", "answered_fields")
        )


if __name__ == "__main__":
    bot = IntakeBot()
    bot.start()
