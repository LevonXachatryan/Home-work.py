from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.conversations = []
    
    def create_conversation(self, user: "User") -> 'Conversation':
        pass
    
    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        conversation.add_message(message)
    
    def receive_message(self, message: 'Message') -> None:
        pass
    
    def manage_settings(self) -> None:
        pass
    
    def get_conversations(self) -> List['Conversation']:
        return self.conversations
    
class Conversation:
    def __init__(self, participants: List['User']):
        self.participants = participants
        self.message_history = []
    
    def add_message(self, message: 'Message') -> None:
        self.message_history.append(message)
    
    def add_user(self, user: 'User') -> None:
        self.participants.append(user)
    
    def get_messages(self) -> List['Message']:
        return self.message_history

class Message(ABC):
    def __init__(self, sender: "User", conversation: "Conversation", timestamp: datetime):
        self.sender = sender
        self.conversation = conversation
        self.timestamp = timestamp
    
    @abstractmethod
    def display_content(self) -> None:
        pass
    
    @abstractmethod
    def get_message_type(self) -> str:
        pass

class TextMessage(Message):
    def __init__(self, sender: User, conversation: Conversation, timestamp: datetime, content: str):
        super().__init__(sender, conversation, timestamp)
        self.content = content
    
    def display_content(self) -> None:
        print(self.sender.name, self.content)
    
    def get_message_type(self) -> str:
        return "Text"

class MultimediaMessage(Message):
    def __init__(self, sender: User, conversation: Conversation, timestamp: datetime, file_path: str, media_type: str):
        super().__init__(sender, conversation, timestamp)
        self.file_path =file_path
        self.media_type = media_type
        
    def display_content(self) -> None:
        print(self.file_path, self.media_type)
    
    def get_message_type(self) -> str:
        return self.media_type

class MessagingManager(ABC):
    @abstractmethod
    def send_message(self, message: 'Message') -> None:
        pass
    @abstractmethod
    def receive_message(self, message: 'Message') -> None :
        pass
    @abstractmethod
    def view_conversation_history(self, conversation: 'Conversation') -> List['Message']:
        pass