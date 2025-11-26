import json
import os
import subprocess
import sys

CONFIG_FILE = "prompts_config.json"

def install_models():
    # 1. Check if config exists
    if not os.path.exists(CONFIG_FILE):
        print(f"❌ Error: '{CONFIG_FILE}' not found!")
        return

    print(f"📖 Reading {CONFIG_FILE}...")
    
    try:
        # 2. Parse the JSON to find the models
        with open(CONFIG_FILE, 'r') as f:
            data = json.load(f)
            # We only care about the values (the backend model names)
            models = list(data.get("llm_map", {}).values())
            
        if not models:
            print("⚠️ No models found in 'llm_map'.")
            return

        print(f"🔍 Found {len(models)} required models: {', '.join(models)}")
        
        # 3. Loop through and pull each model
        for model in models:
            print(f"\n⬇️  Pulling model: {model} ...")
            # This runs the command on the HOST machine directly
            try:
                subprocess.run(["ollama", "pull", model], check=True)
                print(f"✅ {model} ready!")
            except FileNotFoundError:
                print("❌ Error: Ollama is not installed or not in PATH.")
                return
            except subprocess.CalledProcessError:
                print(f"❌ Failed to pull {model}.")

        print("\n🎉 All models are installed! You can now run 'docker-compose up'.")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    install_models()