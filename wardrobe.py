


# A simple Wardrobe Architect MVP

def suggest_outfit(weather, occasion):
    # Basic logic for a Dark Academia aesthetic
    outfit = []
    
    if weather == "cold":
        outfit.append("Brown Wool Trousers")
        outfit.append("Cream Cable-knit Sweater Vest")
    else:
        outfit.append("Chino Trousers")
        outfit.append("Light Cotton Button-down")

    if occasion == "formal":
        outfit.append("Silk Striped Tie")
        outfit.append("Leather Brogues")
    else:
        outfit.append("Loafers")

    return outfit

# Simple User Interaction
print("--- Wardrobe Architect v1.0 ---")
w = input("How is the weather? (cold/warm): ").lower()
o = input("What is the occasion? (formal/casual): ").lower()

recommendation = suggest_outfit(w, o)

print("\nYour Smart Style for today:")
for item in recommendation:
    print(f"- {item}")