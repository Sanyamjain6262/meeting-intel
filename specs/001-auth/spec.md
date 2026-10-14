# 001: Auth

Status: Draft (stub — expand when 000 is Done)

## Goal

Users can register and log in, and the API can tell who is calling. Every later feature attaches data to a user.

## Draft acceptance criteria

- **AC-1** Given a new email and a valid password, when I `POST /auth/register`, then a user is created and I get 201; a duplicate email gives 409.
- **AC-2** Passwords are stored only as Argon2 hashes.
- **AC-3** Given correct credentials, when I `POST /auth/login`, then I get a JWT access token; wrong credentials give 401 with the same message for unknown email and wrong password.
- **AC-4** Given a valid token, when I `GET /auth/me`, then I get my user; a missing, malformed or expired token gives 401.
- **AC-5** A reusable dependency gives any route the current user.

## Out of scope

Password reset, email verification, social login, refresh tokens.

## Dependencies

000.

## Open questions

- Token lifetime, and whether the dashboard uses a cookie or a header.
