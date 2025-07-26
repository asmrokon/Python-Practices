import pyautogui
import time
import random
import pyperclip
import json
import os
from datetime import datetime
import logging

class QuoteBot:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.load_config()
        self.setup_logging()
        self.quotes = self.load_quotes()
        self.used_quotes = set()
        self.spam_patterns = self.load_spam_patterns()
        
    def load_config(self):
        """Load configuration from JSON file"""
        default_config = {
            "message_prefix": ">>> ",
            "min_delay": 2,
            "max_delay": 5,
            "initial_delay": 2,
            "max_messages": 100,
            "avoid_repeats": True,
            "log_messages": True,
            "test_mode": "normal",  # normal, burst, flood, pattern, mixed
            "burst_count": 5,
            "burst_delay": 0.1,
            "flood_rate": 0.5,
            "pattern_repeat": 3,
            "similar_message_chance": 0.3,
            "caps_chance": 0.2,
            "spam_words_chance": 0.1
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    self.config = {**default_config, **json.load(f)}
            except json.JSONDecodeError:
                print(f"Error reading {self.config_file}, using defaults")
                self.config = default_config
        else:
            self.config = default_config
            self.save_config()
    
    def save_config(self):
        """Save current configuration to JSON file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def setup_logging(self):
        """Set up logging if enabled"""
        if self.config.get('log_messages', True):
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler('quote_bot.log'),
                    logging.StreamHandler()
                ]
            )
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = None
    
    def load_spam_patterns(self):
        """Load spam testing patterns"""
        return {
            "spam_words": ["FREE", "CLICK HERE", "URGENT", "LIMITED TIME", "ACT NOW", "WINNER", "CONGRATULATIONS"],
            "repeat_chars": ["!!!", "???", "...", "~~~", "***"],
            "similar_messages": [
                "Check this out!",
                "Check this out!!",
                "CHECK THIS OUT!",
                "check this out",
                "Ch3ck th1s 0ut!"
            ],
            "flood_messages": [
                "SPAM TEST 1",
                "SPAM TEST 2", 
                "SPAM TEST 3",
                "TESTING FLOOD DETECTION",
                "RAPID MESSAGE TEST"
            ]
        }
    
    def load_quotes(self):
        """Load quotes from file or use default list"""
        quotes_file = 'quotes.json'
        
        if os.path.exists(quotes_file):
            try:
                with open(quotes_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Error reading {quotes_file}, using default quotes")
        
        # Default quotes (your original list)
        return [
            "If you win, you live. If you lose, you die. If you don't fight, you can't win. - Eren Yeager",
            "The world is merciless, and it's also very beautiful. - Mikasa Ackerman",
            "A lesson without pain is meaningless. That's because you can't gain something without sacrificing something in return. - Edward Elric",
            "The only thing we're allowed to do is to believe that we won't regret the choice we made. - Levi Ackerman",
            "Chaos isn't a pit. Chaos is a ladder. - Petyr Baelish",
            "When you play the game of thrones, you win or you die. - Cersei Lannister",
            "The things I do for love. - Jaime Lannister",
            "A lion doesn't concern itself with the opinion of sheep. - Tywin Lannister",
            "Winter is coming. - Ned Stark",
            "The night is dark and full of terrors. - Melisandre",
            "Fear cuts deeper than swords. - Arya Stark",
            "Power resides where men believe it resides. - Varys",
            "The world is full of monsters with friendly faces. - Reiner Braun",
            "The only true fear is fear itself. - Hange Zoë",
            "You should enjoy the little things in life, for one day you may look back and realize they were the big things. - Kurt Vonnegut",
            "The freedom to make decisions is the freedom to make mistakes. - Armin Arlert",
            "Every flight begins with a fall. - Hange Zoë",
            "A mind needs books as a sword needs a whetstone. - Tyrion Lannister",
            "When you tear out a man's tongue, you are not proving him a liar, you're only telling the world that you fear what he might say. - Tyrion Lannister",
            "The good ones always die young. - Sasha Blouse",
            "I want to see and understand the world outside. - Historia Reiss",
            "A girl is Arya Stark of Winterfell. And I'm going home. - Arya Stark",
            "There is only one war that matters—the Great War. And it is here. - Jon Snow",
            "A reader lives a thousand lives before he dies. The man who never reads lives only one. - Jojen Reed",
            "People die when they are killed. - Eren Yeager",
            "You cannot hope to bribe or twist... thank God! I've paid my debts. - Tyrion Lannister",
            "There's always another secret. - Vin",
            "Don't be ashamed of who you are. - Kelsier",
            "Sometimes the prize is not worth the costs. - Sazed",
            "I promise you, the world is changing. And the things we fear most may be what save us. - Vin",
            "The most important step a man can take is always the next one. - Kelsier",
            "You should never be ashamed of what you truly are. - Kelsier",
            "The only real freedom you have is the freedom to make mistakes. - Sazed",
            "You want to know what's wrong with the world? Everyone lies. - Vin",
            "We're all broken in some way. The question is what you do with the pieces. - Vin",
            "Sometimes, you have to do what's right, not what's easy. - Kelsier",
            "True strength is found in the moments when you want to give up but you keep going anyway. - Vin",
            "There is always hope. You just have to find it. - Sazed",
            "Faith isn't about knowing. It's about believing. - Sazed",
            "The best lies are those that contain a grain of truth. - Kelsier",
            "Power comes at a cost, and you must be willing to pay the price. - Vin",
            "In this world, everyone wears a mask. - Klein Moretti",
            "Secrets are the currency of power. - Klein Moretti",
            "The world hides many truths, but it always reveals itself to those who seek. - Klein Moretti",
            "Knowledge is the key to survival in the shadows. - Sherlock",
            "Sometimes the truth is more terrifying than any lie. - Klein Moretti",
            "Destiny is not set in stone; it is carved by the choices we make. - Klein Moretti",
            "In the game of secrets, trust is the rarest treasure. - Klein Moretti",
            "Power is meaningless without control. - Klein Moretti",
            "Even the smallest actions can change the course of fate. - Klein Moretti",
            "When you walk through darkness, be the light that guides your way. - Klein Moretti",
            "We are but pawns in a greater game, but pawns with the power to change the board. - Klein Moretti",
            "Hope is a fragile thing, but it is all we have sometimes. - Klein Moretti",
            "The past is a shadow that stretches long, but it cannot dictate your future. - Klein Moretti",
            "No one escapes the consequences of their choices, but some learn faster than others. - Klein Moretti",
            "Fear is a tool; wield it wisely or be consumed by it. - Klein Moretti",
            "The road to truth is paved with illusions and lies. - Klein Moretti",
            "In silence, the loudest secrets are kept. - Klein Moretti",
            "True power comes not from what you control, but from what you understand. - Klein Moretti",
            "To survive in the mist, one must learn to embrace the unknown. - Klein Moretti",
            "The eyes may see, but the soul perceives. - Klein Moretti",
            "The future is built on the dreams we dare to dream. - Kenji Endo",
            "Sometimes the truth hides behind the biggest lies. - Friend",
            "We all have our roles to play, no matter how small. - Maruo",
            "The past is a mystery we must unravel to save tomorrow. - Kenji Endo",
            "Friendship is the strongest weapon we have against the darkness. - Kenji Endo",
            "Sometimes to save the world, we have to lose ourselves first. - Kenji Endo",
            "Even the smallest actions can echo through time. - Friend",
            "Hope is a fragile thing, but it keeps us moving forward. - Maruo",
            "In the end, the real enemy is fear itself. - Kenji Endo",
            "The fate of many rests in the hands of the few who dare to fight. - Friend",
            "You were born to be a sacrifice. - Griffith",
            "Dreams are like the wind; they cannot be held, but they carry us forward. - Guts",
            "The only thing we're allowed to do is to believe that we won't regret the choice we made. - Guts",
            "Struggle is what makes life worth living. - Guts",
            "In this world, the weak are meat, and the strong eat. - Griffith",
            "Sometimes, the hardest battles are the ones within ourselves. - Casca",
            "Fate is cruel, but we are crueler. - Guts",
            "Revenge is the sweetest pleasure that follows pain. - Guts",
            "I have no dreams anymore. No hopes, no plans. I live for the moment. - Guts",
            "The world is full of evil, but it's up to us to fight it. - Guts",
            "A single person can change the course of history. - Kenji Endo",
            "Sometimes the greatest monsters are the people we trust. - Friend",
            "To protect what you love, you must first understand your own fears. - Maruo",
            "The world isn't saved by heroes, but by those who refuse to give up. - Kenji Endo",
            "Memories can be both a curse and a blessing. - Friend",
            "Every generation has its own battles to fight. - Kenji Endo",
            "The truth is a double-edged sword; it can free or destroy. - Maruo",
            "Friendship and hope can light even the darkest paths. - Kenji Endo",
            "We fight because the future depends on us. - Friend",
            "Sometimes you must lose yourself to find the real truth. - Kenji Endo",
            "What is broken can be reforged stronger than before. - Guts",
            "The pain of loss is the price of love. - Casca",
            "Hatred is a fire that burns within, fueling strength and despair alike. - Guts",
            "In the end, all we have are the choices we make. - Griffith",
            "Even in darkness, the human spirit can find its way. - Guts",
            "The scars we carry tell the story of our survival. - Guts",
            "To live is to fight, to fight is to survive. - Guts",
            "True strength is standing despite the pain. - Casca",
            "Destiny is cruel, but so am I. - Guts",
            "In a world without mercy, kindness is rebellion. - Guts"
        ]
    
    def get_random_quote(self):
        """Get a random quote, avoiding repeats if configured"""
        if self.config.get('avoid_repeats', True):
            available_quotes = [q for q in self.quotes if q not in self.used_quotes]
            
            # Reset used quotes if we've used them all
            if not available_quotes:
                self.used_quotes.clear()
                available_quotes = self.quotes
            
            quote = random.choice(available_quotes)
            self.used_quotes.add(quote)
            return quote
        else:
            return random.choice(self.quotes)
    
    def send_message(self, message):
        """Send a message using pyautogui"""
        try:
            pyperclip.copy(message)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            return True
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error sending message: {e}")
            return False
    
    def generate_spam_message(self, base_message):
        """Generate spam-like variations of a message for testing"""
        message = base_message
        
        # Add caps randomly
        if random.random() < self.config.get('caps_chance', 0.2):
            message = message.upper()
        
        # Add spam words
        if random.random() < self.config.get('spam_words_chance', 0.1):
            spam_word = random.choice(self.spam_patterns['spam_words'])
            message = f"{spam_word} {message}"
        
        # Add repeat characters
        if random.random() < 0.3:
            repeat_char = random.choice(self.spam_patterns['repeat_chars'])
            message = f"{message}{repeat_char}"
        
        return message
    
    def run_burst_test(self):
        """Send messages in quick bursts to test burst detection"""
        burst_count = self.config.get('burst_count', 5)
        burst_delay = self.config.get('burst_delay', 0.1)
        
        for i in range(burst_count):
            quote = self.get_random_quote()
            message = self.config['message_prefix'] + quote
            
            if self.send_message(message):
                if self.logger:
                    self.logger.info(f"Burst message {i+1}/{burst_count}: {quote[:30]}...")
                print(f"Burst message {i+1}/{burst_count} sent")
            
            time.sleep(burst_delay)
    
    def run_flood_test(self):
        """Send messages rapidly to test flood detection"""
        flood_rate = self.config.get('flood_rate', 0.5)
        message_count = 0
        max_messages = self.config['max_messages']
        
        while message_count < max_messages:
            flood_msg = random.choice(self.spam_patterns['flood_messages'])
            message = self.config['message_prefix'] + flood_msg + f" #{message_count + 1}"
            
            if self.send_message(message):
                message_count += 1
                if self.logger:
                    self.logger.info(f"Flood message {message_count}: {flood_msg}")
                print(f"Flood message {message_count} sent")
            
            time.sleep(flood_rate)
    
    def run_pattern_test(self):
        """Send similar messages to test pattern detection"""
        pattern_repeat = self.config.get('pattern_repeat', 3)
        similar_messages = self.spam_patterns['similar_messages']
        
        message_count = 0
        max_messages = self.config['max_messages']
        
        while message_count < max_messages:
            # Send each similar message multiple times
            for similar_msg in similar_messages:
                for _ in range(pattern_repeat):
                    if message_count >= max_messages:
                        break
                    
                    message = self.config['message_prefix'] + similar_msg
                    
                    if self.send_message(message):
                        message_count += 1
                        if self.logger:
                            self.logger.info(f"Pattern message {message_count}: {similar_msg}")
                        print(f"Pattern message {message_count} sent")
                    
                    delay = random.uniform(self.config['min_delay'], self.config['max_delay'])
                    time.sleep(delay)
                
                if message_count >= max_messages:
                    break
    
    def run_mixed_test(self):
        """Mix different spam patterns to test comprehensive detection"""
        message_count = 0
        max_messages = self.config['max_messages']
        
        test_types = ['normal', 'burst', 'similar', 'spam_words']
        
        while message_count < max_messages:
            test_type = random.choice(test_types)
            
            if test_type == 'normal':
                quote = self.get_random_quote()
                message = self.config['message_prefix'] + quote
                
                if self.send_message(message):
                    message_count += 1
                    print(f"Normal message {message_count} sent")
                
                delay = random.uniform(self.config['min_delay'], self.config['max_delay'])
                time.sleep(delay)
            
            elif test_type == 'burst':
                remaining_messages = max_messages - message_count
                burst_size = min(self.config.get('burst_count', 5), remaining_messages)
                
                for i in range(burst_size):
                    quote = self.get_random_quote()
                    message = self.generate_spam_message(self.config['message_prefix'] + quote)
                    
                    if self.send_message(message):
                        message_count += 1
                        print(f"Burst message {message_count} sent")
                    
                    time.sleep(self.config.get('burst_delay', 0.1))
                
                # Longer pause after burst
                time.sleep(random.uniform(3, 8))
            
            elif test_type == 'similar':
                similar_msg = random.choice(self.spam_patterns['similar_messages'])
                message = self.config['message_prefix'] + similar_msg
                
                if self.send_message(message):
                    message_count += 1
                    print(f"Similar message {message_count} sent")
                
                time.sleep(random.uniform(0.5, 2))
            
            elif test_type == 'spam_words':
                quote = self.get_random_quote()
                message = self.generate_spam_message(self.config['message_prefix'] + quote)
                
                if self.send_message(message):
                    message_count += 1
                    print(f"Spam-like message {message_count} sent")
                
                time.sleep(random.uniform(1, 3))
    
    def run(self):
        """Main bot loop with different test modes"""
        test_mode = self.config.get('test_mode', 'normal')
        
        print(f"Quote Bot starting in {test_mode} mode...")
        print(f"Initial delay: {self.config['initial_delay']} seconds")
        print(f"Max messages: {self.config['max_messages']}")
        print("Press Ctrl+C to stop")
        
        time.sleep(self.config['initial_delay'])
        
        try:
            if test_mode == 'burst':
                print("Running burst test (rapid message bursts)...")
                self.run_burst_test()
            elif test_mode == 'flood':
                print("Running flood test (continuous rapid messages)...")
                self.run_flood_test()
            elif test_mode == 'pattern':
                print("Running pattern test (similar/repeated messages)...")
                self.run_pattern_test()
            elif test_mode == 'mixed':
                print("Running mixed test (combination of spam patterns)...")
                self.run_mixed_test()
            else:  # normal mode
                print("Running normal mode...")
                self.run_normal_mode()
                
        except KeyboardInterrupt:
            print("\nBot stopped by user")
            if self.logger:
                self.logger.info("Bot stopped by user")
        except Exception as e:
            print(f"Error occurred: {e}")
            if self.logger:
                self.logger.error(f"Bot error: {e}")
    
    def run_normal_mode(self):
        """Original normal message sending mode"""
        message_count = 0
        max_messages = self.config['max_messages']
        
        while message_count < max_messages:
            quote = self.get_random_quote()
            message = self.config['message_prefix'] + quote
            
            if self.send_message(message):
                message_count += 1
                if self.logger:
                    self.logger.info(f"Sent message {message_count}/{max_messages}: {quote[:50]}...")
                print(f"Sent message {message_count}/{max_messages}")
            
            # Random delay between messages
            delay = random.uniform(self.config['min_delay'], self.config['max_delay'])
            time.sleep(delay)
    
    def add_quote(self, quote):
        """Add a new quote to the collection"""
        self.quotes.append(quote)
        # Save to file
        with open('quotes.json', 'w') as f:
            json.dump(self.quotes, f, indent=2)
        print(f"Added quote: {quote}")
    
    def interactive_mode(self):
        """Interactive mode for managing quotes"""
        while True:
            print("\n=== Quote Bot Menu ===")
            print("1. Run bot")
            print("2. Add new quote")
            print("3. Show random quote")
            print("4. Show config")
            print("5. Edit config")
            print("6. Test Mode Selection")
            print("7. Exit")
            
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                self.run()
            elif choice == '2':
                quote = input("Enter new quote: ").strip()
                if quote:
                    self.add_quote(quote)
            elif choice == '3':
                print(f"Random quote: {self.get_random_quote()}")
            elif choice == '4':
                print("Current configuration:")
                for key, value in self.config.items():
                    print(f"  {key}: {value}")
            elif choice == '5':
                self.edit_config()
            elif choice == '6':
                self.select_test_mode()
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def select_test_mode(self):
        """Select different test modes for spam detection"""
        print("\n=== Test Mode Selection ===")
        print("1. Normal - Regular message sending")
        print("2. Burst - Send messages in quick bursts")
        print("3. Flood - Continuous rapid messages")
        print("4. Pattern - Similar/repeated messages")
        print("5. Mixed - Combination of spam patterns")
        
        mode_choice = input("Select test mode (1-5): ").strip()
        
        modes = {
            '1': 'normal',
            '2': 'burst', 
            '3': 'flood',
            '4': 'pattern',
            '5': 'mixed'
        }
        
        if mode_choice in modes:
            self.config['test_mode'] = modes[mode_choice]
            self.save_config()
            print(f"Test mode set to: {modes[mode_choice]}")
            
            # Show relevant settings for selected mode
            if mode_choice == '2':
                print(f"Burst settings: {self.config.get('burst_count', 5)} messages with {self.config.get('burst_delay', 0.1)}s delay")
            elif mode_choice == '3':
                print(f"Flood settings: {self.config.get('flood_rate', 0.5)}s between messages")
            elif mode_choice == '4':
                print(f"Pattern settings: {self.config.get('pattern_repeat', 3)} repeats per message")
        else:
            print("Invalid choice")
    
    def edit_config(self):
        """Edit configuration interactively"""
        print("\nCurrent configuration:")
        for key, value in self.config.items():
            print(f"  {key}: {value}")
        
        key = input("\nEnter config key to edit (or press Enter to cancel): ").strip()
        if key in self.config:
            current_value = self.config[key]
            new_value = input(f"Enter new value for {key} (current: {current_value}): ").strip()
            
            # Try to convert to appropriate type
            try:
                if isinstance(current_value, bool):
                    self.config[key] = new_value.lower() in ['true', '1', 'yes', 'on']
                elif isinstance(current_value, int):
                    self.config[key] = int(new_value)
                elif isinstance(current_value, float):
                    self.config[key] = float(new_value)
                else:
                    self.config[key] = new_value
                
                self.save_config()
                print(f"Updated {key} to {self.config[key]}")
            except ValueError:
                print(f"Invalid value for {key}")
        elif key:
            print(f"Config key '{key}' not found")

if __name__ == "__main__":
    bot = QuoteBot()
    bot.interactive_mode()
