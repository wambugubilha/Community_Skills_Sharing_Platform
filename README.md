# Community_Skills_Sharing_Platform
This project aims at building a platform where the community can come together and share the skills milestones they  have made to build reputable careers.
# Skills App (CRUD)
Implement a Skill model linked to the user.
Each skill includes title, description, category, and creation date.
Added full CRUD API endpoints using Django REST Framework.
# Endpoints 
GET /api/skills/ → List all skills

POST /api/skills/ → Create skill

GET /api/skills/{id}/ → Retrieve skill

PUT /api/skills/{id}/ → Update skill

DELETE /api/skills/{id}/ → Delete skill
# Messaging App
Created a Message model for user-to-user communication.
Each message stores sender, receiver, text, and timestamp.
Implemented API endpoints for sending and viewing messages
# Endpoints
GET /api/messages/ → View inbox/sent messages
POST /api/messages/ → Send message