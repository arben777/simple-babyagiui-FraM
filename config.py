# config.py
# This is a dictionary where keys are investor names and values are lists of example prompts for that investor.
investor_specific_prompts = {
    "Frank Mozzicato": {
        "objectives": [
            "Master the art of the 'Knuckleball of Doom'.",
            "Become the 'Base-Stealing Whisperer'.",
            "Develop the 'Seventh-Inning Zen'."
        ],
        "tasks": [
            "Find a knuckleball guru and schedule a one-on-one session. Make sure to bring a catcher who doesn't mind a few bruises.",
            "Analyze videos of the top 5 base stealers and note their techniques.",
            "Book a meditation session with a Buddhist monk who's also a baseball fan."
        ]
    },
    "InvestorB": {
        "objectives": ["Objective 1 for InvestorB", "Objective 2 for InvestorB", "Objective 3 for InvestorB"],
        "tasks": ["Task 1 for InvestorB", "Task 2 for InvestorB", "Task 3 for InvestorB"]
    },
    # Add more investors and their specific tasks as needed
}
# Default investor - change this before sending to a specific investor.
DEFAULT_INVESTOR = "Frank Mozzicato"