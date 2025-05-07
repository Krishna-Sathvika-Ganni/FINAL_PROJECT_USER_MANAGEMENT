# HELLO PROFESSOR!! THIS IS MY FINAL PROJECT - USER MANAGEMENT!!

## PROJECT CONTENTS:

- [📝 MY LEARNINGS FROM THIS COURSE](#-my-learnings-from-this-course)
- [💼 MY EXPERIENCE WORKING ON THIS PROJECT](#-my-experience-working-on-this-project)
- [🛠️ PROJECT SETUP](#️-project-setup)
- [🐞 QA ISSUES](#-qa-issues)
    - [🔄 ISSUE 1: Mismatch of the Nickname](#-issue-1-mismatch-of-the-nickname)
    - [📧 ISSUE 2: User ID passed as None in the Verification Email](#-issue-2-user-id-passed-as-none-in-the-verification-email)
    - [🔑 ISSUE 3: Verification Token Missing or Invalid](#-issue-3-verification-token-missing-or-invalid)
    - [👮 ISSUE 4: Role Changes from Admin to Authenticated](#-issue-4-role-changes-from-admin-to-authenticated)
    - [🔐 ISSUE 5: Confusing Login Prompt Asking for "Username" Instead of "Email"](#-issue-5-confusing-login-prompt-asking-for-username-instead-of-email)
    - [🖼️ ISSUE 6: Image Upload Endpoint Accepts All File Types Instead of Only Images](#️-issue-6-image-upload-endpoint-accepts-all-file-types-instead-of-only-images)
- [🌄 FEATURE: Profile Picture Upload with Minio](#-feature-profile-picture-upload-with-minio)
- [✅ TEST CASES](#-test-cases)
    - [📤 TEST CASE 1: Basic Upload Functionality for Minio Image](#-test-case-1-basic-upload-functionality-for-minio-image)
    - [🔗 TEST CASE 2: URL Generation for Minio Image](#-test-case-2-url-generation-for-minio-image)
    - [📁 TEST CASE 3: Long Filename Handling for Minio Image](#-test-case-3-long-filename-handling-for-minio-image)
    - [🗂️ TEST CASE 4: Custom Bucket Configuration for Minio Image](#️-test-case-4-custom-bucket-configuration-for-minio-image)
    - [📝 TEST CASE 5: URL Format Variations for Minio Image](#-test-case-5-url-format-variations-for-minio-image)
    - [📋 TEST CASE 6: List Users with Pagination](#-test-case-6-list-users-with-pagination)
    - [❌ TEST CASE 7: Create User with Missing Email Field](#-test-case-7-create-user-with-missing-email-field)
    - [🔒 TEST CASE 8: Create User with Short Password](#-test-case-8-create-user-with-short-password)
    - [🚫 TEST CASE 9: Invalid Token Access](#-test-case-9-invalid-token-access)
    - [⛔ TEST CASE 10: Unauthorized User Update Attempt](#-test-case-10-unauthorized-user-update-attempt)
- [🐳 DOCKERHUB DEPLOYMENT](#-dockerhub-deployment)
- [🌱 WORKING OF THE WHOLE PROJECT](#-working-of-the-project)
- [🏁 FINAL REMARKS](#-final-remarks)
- [📋 FULL DOCUMENTATION](#-full-documentation)


#### 📝 MY LEARNINGS FROM THIS COURSE

- I have learned many practical skills in this course, starting with how to use GitHub effectively for version control and collaboration. 
- The course introduced me to a lot of tools and ideas that I did not know about before, and made me learn a lot more about building, testing, and deploying realistic applications.
- The midterm calculator project was a stepping block that enabled me to get acquainted with the development process and prepare myself for the challenges of this Epic User Management project.


#### 💼 MY EXPERIENCE WORKING ON THIS PROJECT: 
- Throughout the User Management Project, I gained first-hand experience in debugging, clean code writing, user authentication, media upload handling, and integration with third-party storage services like Minio. 
- I also understood the importance of writing thorough test cases and ensuring quality with automated tests and issue tracking. 
- This experience not only improved my technical skills but also made me understand how to approach problems in a systematic manner and work as part of a team.
- Most significantly, I achieved a very high level of confidence in creating production-grade applications that are secure, sustainable, and ready for production.


#### 🛠️ PROJECT SETUP:

1. **FORK AND CLONE THE REPOSITORY**: ```git clone https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT.git``` 

2. **ENVIRONMENT CONFIGURATION:**
    - Create a local `.env` file.
    - And add the MailTrap SMTP settings for testing email features

3. **DATABASE MIGRATION:** ```docker compose exec fastapi alembic upgrade head```

4. **Start the project with Docker**: ```docker compose up --build```

5. **ACCESS POINTS**

- **User Management API:** `localhost/docs`
- **PGAdmin:** `localhost:5050`
- **Minio Console:** `localhost:9001`

6. **USEFUL COMMANDS**

- **To view logs for FastAPI service:** ```docker compose logs fastapi -f```

- **Execute all tests inside the container:** ```docker compose exec fastapi pytest```


#### 🐞 QA ISSUES:


#### 🔄 ISSUE 1: Mismatch of the Nickname

**Description:** 
- The issue is that the Create User API doesn't match the nickname stored in the database input to the request.
- It is also seen as inconsistent with API reaction and example values.
- The Nickname gets overwritten during processing, leading to inconsistencies between input, stored data and output.

**Link to the Issue Report with Screenshots:** [Mismatch of the Nickname Report](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/%F0%9F%94%84%20ISSUE%201.pdf)

**Link to the Issue:** [Mismatch of the Nickname](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/2)

#### 📧 ISSUE 2: User ID passed as None in the Verification Email

**Description:**
- At the time of user registration, the email verification link was generated with a None user ID.
- Thus the email link becomes invalid or incomplete.

**Link to the Issue Report with Screenshots:** [User ID passed as None in the Verification Email Report](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/%F0%9F%93%A7%20ISSUE%202.pdf)

**Link to the Issue:** [User ID passed as None in the Verification Email](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/4)

#### 🔑 ISSUE 3: Verification Token Missing or Invalid

**Description:**
- User is getting a 400: Invalid or expired token for verification error.
- The verification URL is also "None," i.e., token is not being generated, not being stored, or is not being placed properly inside email verification link.

**Link to the Issue Report with Screenshots:** [Verification Token Missing or Invalid Report](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/%F0%9F%94%91%20ISSUE%203.pdf)

**Link to the Issue:** [Verification Token Missing or Invalid](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/6)

#### 👮 ISSUE 4: Role Changes from Admin to Authenticated

**Description:**
- Whenever an admin user's email was verified, their role was automatically downgraded to "Authenticated". 
- This access control violation was resolved by fixing the buggy logic to preserve the original role.

**Link to the Issue Report with Screenshots:** [Role Changes from Admin to Authenticated Report](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/%F0%9F%91%AE%20ISSUE%204.pdf)

**Link to the Issue:** [Role Changes from Admin to Authenticated](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/8)

#### 🔐 ISSUE 5: Confusing Login Prompt Asking for "Username" Instead of "Email"

**Description:**
- The login prompt asked for a "username" when the system was looking for an email. 
- This inconsistency caused login errors and confusion.

**Link to the Issue Report with Screenshots:** [Confusing Login Prompt Asking for "Username" Instead of "Email" Report](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/%F0%9F%94%90%20ISSUE%205.pdf)

**Link to the Issue:** [Confusing Login Prompt Asking for "Username" Instead of "Email"](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/15)

#### 🖼️ ISSUE 6: Image Upload Endpoint Accepts All File Types Instead of Only Images

**DESCRIPTION:**
- The image upload endpoint was allowing any file type to be uploaded. 
- This was not secure and violated expected behavior. 
- The validation was updated to permit only JPEG, PNG, or WEBP image file types.

**Link to the Issue Report with Screenshots:** [Image Upload Endpoint Accepts All File Types Instead of Only Images Report](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/%F0%9F%96%BCissue%206.pdf)

**Link to the Issue:** [Image Upload Endpoint Accepts All File Types Instead of Only Images](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/13)


#### 🌄 FEATURE: Profile Picture Upload with Minio

**Description:**

- A new functionality was added that allows profile images to be uploaded by users, which are stored in Minio (an S3-compatible object store). 
- The feature includes validations for the supported image types, UUID-based renaming to ensure uniqueness, and accessible image URLs. 
- This greatly enhanced user personalization and cloud storage integration.

    - **Storage:** Uses Minio ( S3-compatible object storage )
    - **Security:** Validates image types ( JPEG, PNG, WEBP only )
    - **Uniqueness:** UUID-based filename generation
    - **Accessbility:** Public image URLs for profile display 

**Link to the Feature Report with working Screenshots:** [Profile Picture Upload with Minio Report](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/%F0%9F%8C%84%20FEATURE.pdf)

**Link to the Feature:** [Profile Picture Upload with Minio](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/11)


#### ✅ TEST CASES:

#### 📤 TEST CASE 1: Basic Upload Functionality for Minio Image

**Description:**
- Ensures that the core image upload to Minio is working and returns a successful image URL.

**Link to the Test Case:** [Basic Upload Functionality for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/18)

#### 🔗 TEST CASE 2: URL Generation for Minio Image 

**Description:**
- Ensures that the get_image_url_from_minio() function returns a valid and well-structured public image URL from a filename.

**Link to the Test Case:** [URL Generation for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/19)

#### 📁 TEST CASE 3: Long Filename Handling for Minio Image

**Description:**
- Tests how the function behaves with extremely long filenames, to make sure they are correctly converted to UUID-based names.

**Link to the Test Case:** [Long Filename Handling for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/20)

#### 🗂️ TEST CASE 4: Custom Bucket Configuration for Minio Image

**Description:**
- Ensures that image uploads correctly utilize a custom bucket name if provided in the configuration.

**Link to the Test Case:** [Custom Bucket Configuration for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/21)

#### 📝 TEST CASE 5: URL Format Variations for Minio Image

**Description:**
- Tests whether different formats of base URLs (e.g., with and without trailing slashes) are properly handled in image URL generation.

**Link to the Test Case:** [URL Format Variations for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/22)

#### 📋 TEST CASE 6: List Users with Pagination

**Description:**
- Tests the endpoint for retrieving users with limit and offset to make sure there is proper pagination of results.

**Link to the Test Case:** [List Users with Pagination](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/23)

#### ❌ TEST CASE 7: Create User with Missing Email Field

**Description:**
- Ensures that user registration fails when the required email field is not given, ensuring proper validation.

**Link to the Test Case:** [Create User with Missing Email Field](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/25)

#### 🔒 TEST CASE 8: Create User with Short Password

**Description:**
- Tests that passwords shorter than the allowed length are correctly rejected when a user registers.

**Link to the Test Case:** [Create User with Short Password](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/26)

#### 🚫 TEST CASE 9: Invalid Token Access

**Description:**
- Test that requests made with an invalid JWT token get blocked with correct unauthorized error.

**Link to the Test Case:** [Invalid Token Access](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/27)

#### ⛔ TEST CASE 10: Unauthorized User Update Attempt

**Description:**
- Prevents a non-admin user from changing the details of another user and ensures proper access control.

**Link to the Test Case:** [Unauthorized User Update Attempt](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/29)


#### 🐳 DOCKERHUB DEPLOYMENT:

- The application was successfully containerized and deployed to DockerHub.

**DockerHub Repository:** https://hub.docker.com/r/krisa1329/user_management

![image](https://github.com/user-attachments/assets/20971005-9cf1-44fe-9c69-cb0e2c266fb0)


#### 🌱 WORKING OF THE PROJECT:

**Link to the Working of the Project Screenshots:** [ Working of the Project Report](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/%F0%9F%8C%B1%20WORKING%20OF%20THE%20WHOLE%20PROJECT.pdf)


#### 🏁 FINAL REMARKS:

This project was a significant milestone in my learning. It challenged me to debug, test, and apply DevOps concepts. The iterative development and QA process mimicked real-world processes and has enhanced my technical and collaboration skills.


#### 📋 FULL DOCUMENTATION:

- [FINAL USER MANAGEMENT DOCUMENTATION ( .docx )](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/FINAL%20USER%20MANAGEMENT%20PROJECT%20DOCUMENTATION.docx)
- [FINAL USER MANAGEMENT DOCUMENTATION ( .pdf )](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/blob/main/FINAL%20USER%20MANAGEMENT%20PROJECT%20DOCUMENTATION.pdf)

