## 🤖 ChatGPT Voice Assistant: Your AI Sidekick Speaks! 🎙️

This repository houses a Python script that interacts with ChatGPT in the background, offering a unique voice-assisted experience.

### ✨ Features

- **Background Interaction:** Seamlessly interacts with ChatGPT behind the scenes, retrieving responses without manual intervention.
- **Voice Output:** Utilizes text-to-speech functionality to audibly deliver ChatGPT's responses, creating a conversational atmosphere.
- **Customizable:** Allows for easy modification of input prompts and voice settings to tailor the experience to your preferences.

### 🛠️ Technologies

The script leverages the following libraries:

- **Playwright:** Controls and automates web browser interactions.
- **dotenv:** Manages environment variables for secure storage of credentials.
- **pyttsx3 (Optional):** Enables text-to-speech functionality.

**Note:** You will need to install these libraries using pip: `pip install playwright dotenv pyttsx3`

### 🚀 Getting Started

1.  **Clone the repository:** `git clone https://github.com/MohamedAbdelrehem/chatgpt-voice-assistant.git`
2.  **Install dependencies:** `pip install -r requirements.txt`
3.  **Configure credentials:**
    - Create a `.env` file in the project directory.
    - Add your ChatGPT email and password as environment variables:

```
email=your_chatgpt_email
        password=your_chatgpt_password

```

4.  **Run the script:** `python chatgpt_voice_assistant.py`
5.  **Interact with ChatGPT:** Follow the prompts in the console to ask your questions and listen to the responses.

### 🎨 Customization

- **Input Prompts:** Modify the `askQuestion()` function to change how questions are submitted to ChatGPT.
- **Voice Settings:** Explore the `pyttsx3` documentation to adjust voice parameters like speed, volume, and language.

### 🔐 Security

- **Environment Variables:** The `.env` file keeps your ChatGPT credentials secure. Do not share this file publicly.

### 🔭 Future Enhancements

- **Voice Input:** Integrate speech recognition for a completely hands-free experience.
- **Multi-Language Support:** Expand language capabilities for broader accessibility.
- **Customizable Voices:** Implement options for different voice styles and personalities.

### 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests for bug fixes, enhancements, or new features. Let's make this project even more awesome together!
