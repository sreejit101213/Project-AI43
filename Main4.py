from GROQ4 import generate_response

def bias_mitigation_activtity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt that may contain bias (e.g., 'Describe the ideal leader'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return

    initial_response = generate_response(prompt, temperature = 0.3, max_tokens = 1024)
    print(f"\nInitial AI Respoinse: {initial_response}")

    modified_prompt = input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a leader'): ").strip()
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature = 0.3, max_tokens = 1024)
        print(f"\nModified AI Response: {modified_response}")
    else:
        print("No modified prompt provided. Skipping modified response.")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_prompt= input("Enter a long prompt (more than 300 words, e.g., a detailed story or article): ").strip()
    if long_prompt:
        long_response = generate_response(long_prompt, temperature = 0.3, max_tokens = 256)
        preview = (long_response[:500] + '...') if len(long_response) > 500 else long_response
        print(f"\nResponse to Long Prompt: {preview}")
    else:
        print("No long prompt provided. Skipping response.")

    short_prompt = input("Now, condense the prompt to be more concise (e.g., a summary of the story or article): ").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature = 0.3, max_tokens = 256)
        print(f"\nResponse to Condensed Prompt: {short_response}")
    else:
        print("No condensed prompt provided. Skipping response.")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Bias Mitigation")
    print("2) Token Limit")
    choice = input("> ").strip()

    if choice == "1":
        bias_mitigation_activtity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    run_activity()