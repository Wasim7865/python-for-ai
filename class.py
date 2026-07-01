from dotenv import load_dotenv
import os

"""
class pc:
    def __init__(self,cpu,gpu,ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram

user1_pc = pc("AMD Ryzen 5 5500","AMD Radeon RX 6750 XT","16GB DDR4")
user2_pc = pc("AMD Ryzen 9 ThreadRipper","AMD Radeon 9600 XTX","32GB DDR5")

print("The Specs Of the user 1 pc is:")
print(f"Cpu: {user1_pc.cpu}")
print(f"Gpu: {user1_pc.gpu}")
print(f"Ram: {user1_pc.ram}\n")

print("The Specs Of the user 2 pc is:")
print(f"Cpu: {user2_pc.cpu}")
print(f"Gpu: {user2_pc.gpu}")
print(f"Ram: {user2_pc.ram}")
"""

"""
class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad@email")
validator.validate_age(age=200)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']
"""


class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False

    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True


class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length

    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # Truncate if needed
        if len(text) > self.max_length:
            text = text[: self.max_length]
        return f"Processed: {text}"


# Use the model - with named arguments
model = TextModel(model_name="gpt-3.5-turbo")

# Call method - notice no 'self' parameter needed
result = model.process_text(text="Hello world")
print(result)  # Loading gpt-3.5-turbo...
# Processed: Hello world


# Class bundles data and methods
class TextProcessor:
    def __init__(self, text):
        self.text = text

    def clean(self):
        self.text = self.text.strip().lower()
        return self

    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self


# Chain methods on object
processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text
print(result)

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get("API_KEY")
debug = os.environ.get("DEBUG")
database_url = os.environ.get("DATABASE_URL")

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")
print(f"Database: {database_url}")

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    print("Please set OPENAI_API_KEY in .env file")
    exit(1)

# Use the API
headers = {"Authorization": f"Bearer {API_KEY}"}
# Make your API calls...


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]
print(calculate_total(shopping_cart))
