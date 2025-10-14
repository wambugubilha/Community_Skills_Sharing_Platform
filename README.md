# Community_Skills_Sharing_Platform
This project aims at building a platform where the community can come together and share the skills milestones they  have made to build reputable careers.

# User authentication and profile models
Features
-Custom User model with email login (no username).
-Auto-created Profile (bio, location).
-Token Authentication via rest_framework.authtoken.
-Endpoints: register, login, logout, view/update profile.

# Skill Listings (CRUD)
Implemented full CRUD functionality for the Skill model.
Added endpoints for creating, viewing, updating, and deleting skill posts.
Integrated category and user relationships for better data organization.
Finalized database schema and ran migrations successfully.

# Messaging System
Developed direct messaging between users using the Message model.
Created REST API endpoints for sending and retrieving messages.
Added serializers and views to ensure secure, user-to-user communication.

#  Feedback System
Introduced a text-based feedback feature for user interactions.
Linked Feedback model to users (from_user → to_user) for transparency.
Implemented API endpoints for submitting and viewing feedback.
Conducted feature testing to validate messaging and feedback reliability.
