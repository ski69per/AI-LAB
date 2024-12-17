# Function to check entailment based on user input
def check_entailment():
    print("Welcome to the Entailment Checker!")

    # Step 1: Gather user input for facts (Premises)
    alice_is_mother_of_bob = input("Enter the fact: Alice is the mother of Bob. (e.g., 'Alice is the mother of Bob')\n")
    bob_is_father_of_charlie = input("Enter the fact: Bob is the father of Charlie. (e.g., 'Bob is the father of Charlie')\n")
    father_is_parent = input("Enter the fact: A father is a parent. (e.g., 'A father is a parent')\n")
    mother_is_parent = input("Enter the fact: A mother is a parent. (e.g., 'A mother is a parent')\n")
    all_parents_have_children = input("Enter the fact: All parents have children. (e.g., 'All parents have children')\n")
    parents_children_are_siblings = input("Enter the fact: Parents' children are siblings. (e.g., 'Parents' children are siblings')\n")
    alice_is_married_to_david = input("Enter the fact: Alice is married to David. (e.g., 'Alice is married to David')\n")

    # Step 2: Entailment reasoning process
    if ('Alice is the mother of Bob' in alice_is_mother_of_bob and
        'Bob is the father of Charlie' in bob_is_father_of_charlie and
        'A father is a parent' in father_is_parent and
        'A mother is a parent' in mother_is_parent and
        'All parents have children' in all_parents_have_children and
        "Parents' children are siblings" in parents_children_are_siblings and
        'Alice is married to David' in alice_is_married_to_david):

        # Conclusion: Check if Charlie is a sibling of Bob
        print("\nSince Alice is Bob's mother and Bob is Charlie's father, Charlie and Bob are siblings.")
        print("Conclusion: Charlie is a sibling of Bob. The hypothesis is entailed by the knowledge base.")
    else:
        print("\nThe information provided does not fully support the conclusion.")

# Run the function
check_entailment()
