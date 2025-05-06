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

Unresolved:
 
 ![image](https://github.com/user-attachments/assets/4aac5d33-a85f-4743-8d5e-d0cde3a7ae01)

  ![image](https://github.com/user-attachments/assets/627f0c85-73e7-43c1-9a6e-dad939b292ee)

  ![image](https://github.com/user-attachments/assets/722263e2-3acd-4f72-8f10-27db33f0be2c)

 Resolved:

![image](https://github.com/user-attachments/assets/65b65d2c-e95e-4d33-bb38-541761ecd802)

 ![image](https://github.com/user-attachments/assets/fc5db703-8a79-45ed-9f79-6dd59b54b580)

**Link to the Issue:** [Mismatch of the Nickname](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/2)

###### ISSUE 2: User ID passed as None in the Verification Email

**Description:**
- At the time of user registration, the email verification link was generated with a None user ID.
- Thus the email link becomes invalid or incomplete.

Unresolved:

 ![image](https://github.com/user-attachments/assets/54cc5165-006e-4ca9-8a13-131742286a59)


Resolved:
 
 ![image](https://github.com/user-attachments/assets/46ca9e6b-b7a1-4b17-834d-49096ea988c7)

**Link to the Issue:** [User ID passed as None in the Verification Email](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/4)

###### ISSUE 3: Verification Token Missing or Invalid

**Description:**
- User is getting a 400: Invalid or expired token for verification error.
- The verification URL is also "None," i.e., token is not being generated, not being stored, or is not being placed properly inside email verification link.

Unresolved:

 ![image](https://github.com/user-attachments/assets/44d198f7-b193-4fc1-942a-a7b444bf52db)


Resolved:

 ![image](https://github.com/user-attachments/assets/4cd7bb7e-684c-47e9-a711-dc0712c404ce)


**Link to the Issue:** [Verification Token Missing or Invalid](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/6)

###### ISSUE 4: Role Changes from Admin to Authenticated

**Description:**
- Whenever an admin user's email was verified, their role was automatically downgraded to "Authenticated". 
- This access control violation was resolved by fixing the buggy logic to preserve the original role.

Unresolved:

 ![image](https://github.com/user-attachments/assets/331b5278-4be5-484e-b411-776ff3a684c8)


Resolved:

 ![image](https://github.com/user-attachments/assets/3027b72c-9bce-42db-addd-f0cfed5cbac1)

**Link to the Issue:** [Role Changes from Admin to Authenticated](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/8)

###### ISSUE 5: Confusing Login Prompt Asking for "Username" Instead of "Email"

**Description:**
- The login prompt asked for a "username" when the system was looking for an email. 
- This inconsistency caused login errors and confusion.

Resolved:

 ![image](https://github.com/user-attachments/assets/b4f86dec-5cc4-4a40-a66f-9e0a3d4acf8d)



**Link to the Issue:** [Confusing Login Prompt Asking for "Username" Instead of "Email"](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/15)

###### ISSUE 6: Image Upload Endpoint Accepts All File Types Instead of Only Images

**DESCRIPTION:**
- The image upload endpoint was allowing any file type to be uploaded. 
- This was not secure and violated expected behavior. 
- The validation was updated to permit only JPEG, PNG, or WEBP image file types.

Unresolved:

 ![image](https://github.com/user-attachments/assets/21e50656-7ba0-4a3f-9d43-50e8a002961d)


Resolved:

![image](https://github.com/user-attachments/assets/7d659082-93d6-48ea-9712-41cf03fa5763)


**Link to the Issue:** [Image Upload Endpoint Accepts All File Types Instead of Only Images](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/13)


#### FEATURE: 🌄 Profile Picture Upload with Minio

**Description:**
- A new functionality was added that allows profile images to be uploaded by users, which are stored in Minio (an S3-compatible object store). 
- The feature includes validations for the supported image types, UUID-based renaming to ensure uniqueness, and accessible image URLs. 
- This greatly enhanced user personalization and cloud storage integration.

**WORKING OF THE FEATURE:**

 ![image](https://github.com/user-attachments/assets/748cf7bc-07f5-4846-be1d-de5171e59210)

 ![image](https://github.com/user-attachments/assets/b725bef7-ad2c-4b63-9e57-d03d1f455832)

 ![image](https://github.com/user-attachments/assets/910e0044-e077-465a-beb0-dbe077c61423)

 ![image](https://github.com/user-attachments/assets/c26713f2-5e5b-4d96-8c91-08c65392b8b1)

 ![image](https://github.com/user-attachments/assets/a8e1d819-8cad-4e3d-ac37-ecb6da9de1dd)

 ![image](https://github.com/user-attachments/assets/83efcf35-098b-468e-b3b0-63e89e0665a7)

 ![image](https://github.com/user-attachments/assets/ea8115d1-8030-4883-a954-dcc8e665ffe2)

 **Link to the Feature:** [Profile Picture Upload with Minio](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/11)

#### TEST CASES:

###### TEST CASE 1: Basic Upload Functionality for Minio Image

**Description:**
- Ensures that the core image upload to Minio is working and returns a successful image URL.

**Link to the Test Case:** [Basic Upload Functionality for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/18)

###### TEST CASE 2: URL Generation for Minio Image 

**Description:**
- Ensures that the get_image_url_from_minio() function returns a valid and well-structured public image URL from a filename.

**Link to the Test Case:** [URL Generation for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/19)

###### TEST CASE 3: Long Filename Handling for Minio Image

**Description:**
- Tests how the function behaves with extremely long filenames, to make sure they are correctly converted to UUID-based names.

**Link to the Test Case:** [Long Filename Handling for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/20)

###### TEST CASE 4: Custom Bucket Configuration for Minio Image

**Description:**
- Ensures that image uploads correctly utilize a custom bucket name if provided in the configuration.

**Link to the Test Case:** [Custom Bucket Configuration for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/21)

###### TEST CASE 5: URL Format Variations for Minio Image

**Description:**
- Tests whether different formats of base URLs (e.g., with and without trailing slashes) are properly handled in image URL generation.

**Link to the Test Case:** [URL Format Variations for Minio Image](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/22)

###### TEST CASE 6: List Users with Pagination

**Description:**
- Tests the endpoint for retrieving users with limit and offset to make sure there is proper pagination of results.

**Link to the Test Case:** [List Users with Pagination](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/23)

###### TEST CASE 7: Create User with Missing Email Field

**Description:**
- Ensures that user registration fails when the required email field is not given, ensuring proper validation.

**Link to the Test Case:** [Create User with Missing Email Field](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/25)

###### TEST CASE 8: Create User with Short Password

**Description:**
- Tests that passwords shorter than the allowed length are correctly rejected when a user registers.

**Link to the Test Case:** [Create User with Short Password](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/26)

###### TEST CASE 9: Invalid Token Access

**Description:**
- Test that requests made with an invalid JWT token get blocked with correct unauthorized error.

**Link to the Test Case:** [Invalid Token Access](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/27)

###### TEST CASE 10: Unauthorized User Update Attempt

**Description:**
- Prevents a non-admin user from changing the details of another user and ensures proper access control.

**Link to the Test Case:** [Unauthorized User Update Attempt](https://github.com/Krishna-Sathvika-Ganni/FINAL_PROJECT_USER_MANAGEMENT/issues/29)


#### DOCKERHUB DEPLOYMENT:

- The application was successfully containerized and deployed to DockerHub.

**DockerHub Repository:**

https://hub.docker.com/repository/docker/krisa1329/user_management/general

 

![image](https://github.com/user-attachments/assets/20971005-9cf1-44fe-9c69-cb0e2c266fb0)



#### WORKING OF THE PROJECT:

###### USER MANAGEMENT PAGE:

![image](https://github.com/user-attachments/assets/d0499491-6c89-4fec-9142-8773e81dd1b4)

 ![image](https://github.com/user-attachments/assets/adc5316c-1838-4b0f-b6bd-8d7a5cd8a417)

 ![image](https://github.com/user-attachments/assets/bb909ec0-c2f0-417a-9771-161dd7bbc51e)

###### PGADMIN PAGE:

 ![image](https://github.com/user-attachments/assets/8a54df7d-bdcd-4c4b-9292-a215a0ee53cd)


###### MINIO PAGE:

 ![image](https://github.com/user-attachments/assets/6aa26d9c-ac0b-40a0-9066-712ceb8e0e90)

 ![image](https://github.com/user-attachments/assets/4d8f7791-c39c-42f9-868b-b64f7b022960)


###### CREATION OF TABLES IN PGADMIN WITH THE COMMAND:

 ![image](https://github.com/user-attachments/assets/c99c2634-b1dc-416b-9d89-4c974b213b84)


###### REGISTERING OF USER:

 ![image](https://github.com/user-attachments/assets/b14ecd5a-f6ff-49d2-83f0-dd585d68d181)

  ![image](https://github.com/user-attachments/assets/71797b34-ba7b-4057-a093-a9fcfbdaf19b)



###### REGISTERED USER STORED IN DATABASE:

 ![image](https://github.com/user-attachments/assets/c1ea5acf-db88-450a-bc57-c31e34756f46)


###### VERIFICATION OF REGISTERED USER USING EMAIL:

 ![image](https://github.com/user-attachments/assets/b6c5616c-6d6c-4982-8fb4-3b2a187da62f)

 ![image](https://github.com/user-attachments/assets/7a15652d-9cce-414b-86f5-a7dcecbbf999)

 
 ![image](https://github.com/user-attachments/assets/13c1adea-773a-43b1-9996-b22d5f2c873e)

###### LOGGING IN OF THE REGISTERED USER:

 ![image](https://github.com/user-attachments/assets/7215ddc3-253b-49a4-b2e1-aa2c37a19728)

 ![image](https://github.com/user-attachments/assets/6b12dff3-e216-4735-9ee4-7ae4fadcaf19)

###### AUTHORIZATION OF THE USER:

 ![image](https://github.com/user-attachments/assets/f772f439-581b-4b39-a0dc-d484d6a824a8)


###### PROFILE PICTURE UPLOAD OF THE REGISTERED USER:

 ![image](https://github.com/user-attachments/assets/a2b07264-b9cd-44c0-bb13-3717a54223e1)

 ![image](https://github.com/user-attachments/assets/0f4a089d-de93-4c04-b0f3-283c0a94526e)

 ![image](https://github.com/user-attachments/assets/ed8ed27a-289d-4b13-a156-14608151c3ab)

###### REGISTERING OF ANOTHER USER:

 ![image](https://github.com/user-attachments/assets/489200b4-f8a3-455d-ba28-feefa25118f0)

 ![image](https://github.com/user-attachments/assets/6c2195c3-a5ff-4f43-a054-63230533dca9)

 ![image](https://github.com/user-attachments/assets/3696d1bc-ae3c-49ef-8129-7343398eab6a)


###### VERIFICATION OF ANOTHER USER:

 ![image](https://github.com/user-attachments/assets/6d0abca2-4698-426e-ab1d-be5158e501c1)

 ![image](https://github.com/user-attachments/assets/3e1281fa-c093-4343-9331-9905c6523338)


###### REGISTERED USER STORED IN DATABASE:

 ![image](https://github.com/user-attachments/assets/68c60bbe-92ed-4529-90bc-dbe4a62546ad)


###### PROFILE PICTURE UPLOAD FOR ANOTHER USER:

 ![image](https://github.com/user-attachments/assets/e5be4e6e-2183-4c8b-b230-ee513c4099f9)

###### GETTING THE USER:

  ![image](https://github.com/user-attachments/assets/188fe3ba-b548-4b36-8e2c-eb920f2c4498)

 ![image](https://github.com/user-attachments/assets/d9525455-1cdc-4d41-8f55-dae022455af9)


###### UPDATING THE USER:

  ![image](https://github.com/user-attachments/assets/3b0369e9-ea11-4b95-8797-71763cca7acf)

 ![image](https://github.com/user-attachments/assets/d1278035-43b3-4f71-aac5-4d8b2f14ca87)

 ![image](https://github.com/user-attachments/assets/c4c9c8ed-51db-4a8b-bb86-0fe955f0306b)


###### LISTING THE USERS:

 ![image](https://github.com/user-attachments/assets/58267699-5471-42d1-83be-fe275dde56c2)

 ![image](https://github.com/user-attachments/assets/7bdca0bb-1171-41b0-a5bf-eb1da5d7482a)

 ![image](https://github.com/user-attachments/assets/1676e65c-606b-41f2-8fed-b9d4654c2101)

###### DELETING THE USER:

 ![image](https://github.com/user-attachments/assets/84187015-e198-490f-8248-bd6afeaca454)

 ![image](https://github.com/user-attachments/assets/77a81f14-fa53-40ac-bb77-e0c712874616)

 ![image](https://github.com/user-attachments/assets/33966742-f5c4-4c7f-b1d2-fdbae1cbf957)


#### FINAL REMARKS:

This project was a significant milestone in my learning. It challenged me to debug, test, and apply DevOps concepts. The iterative development and QA process mimicked real-world processes and has enhanced my technical and collaboration skills.

