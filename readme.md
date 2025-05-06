# HELLO PROFESSOR!! THIS IS MY FINAL PROJECT - USER MANAGEMENT!!

# HELLO PROFESSOR!! THIS IS MY FINAL PROJECT - USER MANAGEMENT!!

## PROJECT CONTENTS:

- [MY LEARNINGS FROM THIS COURSE](#my-learnings-from-this-course)
- [MY EXPERIENCE WORKING ON THIS PROJECT](#my-experience-working-on-this-project)
- [PROJECT SETUP](#project-setup)
- [QA ISSUES](#qa-issues)
    - [ISSUE 1: Mismatch of the Nickname](#issue-1-mismatch-of-the-nickname)
    - [ISSUE 2: User ID passed as None in the Verification Email](#issue-2-user-id-passed-as-none-in-the-verification-email)
    - [ISSUE 3: Verification Token Missing or Invalid](#issue-3-verification-token-missing-or-invalid)
    - [ISSUE 4: Role Changes from Admin to Authenticated](#issue-4-role-changes-from-admin-to-authenticated)
    - [ISSUE 5: Confusing Login Prompt Asking for "Username" Instead of "Email"](#issue-5-confusing-login-prompt-asking-for-username-instead-of-email)
    - [ISSUE 6: Image Upload Endpoint Accepts All File Types Instead of Only Images](#issue-6-image-upload-endpoint-accepts-all-file-types-instead-of-only-images)
- [FEATURE: 🌄 Profile Picture Upload with Minio](#feature--profile-picture-upload-with-minio)
- [TEST CASES](#test-cases)
    - [TEST CASE 1: Basic Upload Functionality for Minio Image](#test-case-1-basic-upload-functionality-for-minio-image)
    - [TEST CASE 2: URL Generation for Minio Image](#test-case-2-url-generation-for-minio-image)
    - [TEST CASE 3: Long Filename Handling for Minio Image](#test-case-3-long-filename-handling-for-minio-image)
    - [TEST CASE 4: Custom Bucket Configuration for Minio Image](#test-case-4-custom-bucket-configuration-for-minio-image)
    - [TEST CASE 5: URL Format Variations for Minio Image](#test-case-4-custom-bucket-configuration-for-minio-image)
    - [TEST CASE 6: List Users with Pagination](#test-case-5-url-format-variations-for-minio-image)
    - [TEST CASE 7: Create User with Missing Email Field](#test-case-7-create-user-with-missing-email-field)
    - [TEST CASE 8: Create User with Short Password](#test-case-8-create-user-with-short-password)
    - [TEST CASE 9: Invalid Token Access](#test-case-9-invalid-token-access)
    - [TEST CASE 10: Unauthorized User Update Attempt](#test-case-10-unauthorized-user-update-attempt)
- [DOCKERHUB DEPLOYMENT](#dockerhub-deployment)
- [WORKING OF THE WHOLE PROJECT](#working-of-the-project)
- [FINAL REMARKS](#final-remarks)


#### MY LEARNINGS FROM THIS COURSE
- I have learned many practical skills in this course, starting with how to use GitHub effectively for version control and collaboration. 
- The course introduced me to a lot of tools and ideas that I did not know about before, and made me learn a lot more about building, testing, and deploying realistic applications.
- The midterm calculator project was a stepping block that enabled me to get acquainted with the development process and prepare myself for the challenges of this Epic User Management project.

#### MY EXPERIENCE WORKING ON THIS PROJECT: 
- Throughout the User Management Project, I gained first-hand experience in debugging, clean code writing, user authentication, media upload handling, and integration with third-party storage services like Minio. 
- I also understood the importance of writing thorough test cases and ensuring quality with automated tests and issue tracking. 
- This experience not only improved my technical skills but also made me understand how to approach problems in a systematic manner and work as part of a team.
- Most significantly, I achieved a very high level of confidence in creating production-grade applications that are secure, sustainable, and ready for production.

#### PROJECT SETUP:
- Fork the Professor’s repository.
- Clone the forked repository locally to work.
- Create a local .env file and add your MailTrap SMTP settings. This enables testing of email features during manual testing. (Note: During automated testing with pytest, email sending is mocked and not actually performed.)
- Running pytest will delete the user table, but it does not remove the Alembic migration table, which can lead to sync issues. To resolve: 
    - Drop the Alembic table manually if needed. 
    - Re-run the migration using:

```docker compose exec fastapi alembic upgrade head```

- Start the project with Docker: 

```docker compose up --build```

- Access the User Management website at localhost/docs
- Access PGAdmin at localhost:5050
- Access the Minio at localhost:9001
- To view logs for FastAPI service: 

```docker compose logs fastapi -f```

- Execute all tests inside the container: 

```docker compose exec fastapi pytest```


#### QA ISSUES:

###### ISSUE 1: Mismatch of the Nickname

**Description:** 
- The issue is that the Create User API doesn't match the nickname stored in the database input to the request.
- It is also seen as inconsistent with API reaction and example values.
- The Nickname gets overwritten during processing, leading to inconsistencies between input, stored data and output.

**Link to the Issue:** Mismatch of the Nickname

###### ISSUE 2: User ID passed as None in the Verification Email

**Description:**
- At the time of user registration, the email verification link was generated with a None user ID.
- Thus the email link becomes invalid or incomplete.

**Link to the Issue:** User ID passed as None in the Verification Email

###### ISSUE 3: Verification Token Missing or Invalid

**Description:**
- User is getting a 400: Invalid or expired token for verification error.
- The verification URL is also "None," i.e., token is not being generated, not being stored, or is not being placed properly inside email verification link.

**Link to the Issue:** Verification Token Missing or Invalid

###### ISSUE 4: Role Changes from Admin to Authenticated

**Description:**
- Whenever an admin user's email was verified, their role was automatically downgraded to "Authenticated". 
- This access control violation was resolved by fixing the buggy logic to preserve the original role.

**Link to the Issue:** Role Changes from Admin to Authenticated

###### ISSUE 5: Confusing Login Prompt Asking for "Username" Instead of "Email"

**Description:**
- The login prompt asked for a "username" when the system was looking for an email. 
- This inconsistency caused login errors and confusion. 

**Link to the Issue:** Confusing Login Prompt Asking for "Username" Instead of "Email"

###### ISSUE 6: Image Upload Endpoint Accepts All File Types Instead of Only Images

**DESCRIPTION:**
- The image upload endpoint was allowing any file type to be uploaded. 
- This was not secure and violated expected behavior. 
- The validation was updated to permit only JPEG, PNG, or WEBP image file types.

**Link to the Issue:** Image Upload Endpoint Accepts All File Types Instead of Only Images


#### FEATURE: 🌄 Profile Picture Upload with Minio

**Description:**
- A new functionality was added that allows profile images to be uploaded by users, which are stored in Minio (an S3-compatible object store). 
- The feature includes validations for the supported image types, UUID-based renaming to ensure uniqueness, and accessible image URLs. 
- This greatly enhanced user personalization and cloud storage integration.

**WORKING OF THE FEATURE:**


#### TEST CASES:

###### TEST CASE 1: Basic Upload Functionality for Minio Image

**Description:**
- Ensures that the core image upload to Minio is working and returns a successful image URL.

**Link to the Test Case:** Basic Upload Functionality for Minio Image

###### TEST CASE 2: URL Generation for Minio Image 

**Description:**
- Ensures that the get_image_url_from_minio() function returns a valid and well-structured public image URL from a filename.

**Link to the Test Case:** URL Generation for Minio Image

###### TEST CASE 3: Long Filename Handling for Minio Image

**Description:**
- Tests how the function behaves with extremely long filenames, to make sure they are correctly converted to UUID-based names.

**Link to the Test Case:** Long Filename Handling for Minio Image

###### TEST CASE 4: Custom Bucket Configuration for Minio Image

**Description:**
- Ensures that image uploads correctly utilize a custom bucket name if provided in the configuration.

**Link to the Test Case:** Custom Bucket Configuration for Minio Image

###### TEST CASE 5: URL Format Variations for Minio Image

**Description:**
- Tests whether different formats of base URLs (e.g., with and without trailing slashes) are properly handled in image URL generation.

**Link to the Test Case:** URL Format Variations for Minio Image

###### TEST CASE 6: List Users with Pagination

**Description:**
- Tests the endpoint for retrieving users with limit and offset to make sure there is proper pagination of results.

**Link to the Test Case:** List Users with Pagination

###### TEST CASE 7: Create User with Missing Email Field

**Description:**
- Ensures that user registration fails when the required email field is not given, ensuring proper validation.

**Link to the Test Case:** Create User with Missing Email Field

###### TEST CASE 8: Create User with Short Password

**Description:**
- Tests that passwords shorter than the allowed length are correctly rejected when a user registers.

**Link to the Test Case:** Create User with Short Password

###### TEST CASE 9: Invalid Token Access

**Description:**
- Test that requests made with an invalid JWT token get blocked with correct unauthorized error.

**Link to the Test Case:** Invalid Token Access

###### TEST CASE 10: Unauthorized User Update Attempt

**Description:**
- Prevents a non-admin user from changing the details of another user and ensures proper access control.

**Link to the Test Case:** Unauthorized User Update Attempt


#### DOCKERHUB DEPLOYMENT:

- The application was successfully containerized and deployed to DockerHub.

**DockerHub Repository:**

https://hub.docker.com/repository/docker/krisa1329/user_management/general


#### WORKING OF THE PROJECT:

###### USER MANAGEMENT PAGE:

###### PGADMIN PAGE:

###### MINIO PAGE:

###### CREATION OF TABLES IN PGADMIN WITH THE COMMAND:

###### REGISTERING OF USER:

###### REGISTERED USER STORED IN DATABASE:

###### VERIFICATION OF REGISTERED USER USING EMAIL:

###### LOGGING IN OF THE REGISTERED USER:

###### AUTHORIZATION OF THE USER:

###### PROFILE PICTURE UPLOAD OF THE REGISTERED USER:

###### REGISTERING OF ANOTHER USER:

###### VERIFICATION OF ANOTHER USER:

###### REGISTERED USER STORED IN DATABASE:

###### PROFILE PICTURE UPLOAD FOR ANOTHER USER:

###### GETTING THE USER:

###### UPDATING THE USER:

###### LISTING THE USERS:

###### DELETING THE USER:

#### FINAL REMARKS:

This project was a significant milestone in my learning. It challenged me to debug, test, and apply DevOps concepts. The iterative development and QA process mimicked real-world processes and has enhanced my technical and collaboration skills.

