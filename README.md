# tookie-demo
Django app that demonstrates Cookie based authentication for quick prototypes of Server Side Rendered MVP's which can also work with Token Based Authentication if needed in the future

Creating MVP's with Django almost always deals with server side rendered applications which makes use of Django's built in SessionAuthentication

This app demonstrates authentication flow based on SessionAuthentication that allows the developer to do async API calls from a completely separate frontend while still being authorized as long as both are served from the same domain.
This prepares the developer and the app for further scaling to complex frontends even if it starts with Django's own templating system


Authentication Flow
====
1. **Frontend** (or static html) Serves the login page
2. **Frontend** (or static html) sends the credentials (usually *username* and *password*) along with a **redirect_url** so the backend knows where to redirect the user after authorization
3. **Backend** responds with a link (containg a *token* and the *user ID*) to the frontend where the user is **required to be redirected**
4. Redirection takes the user to a *backend served page* where it verifies the token and *sets the cookie* if successfully verified
5. Upon successful validation it *quickly redirects the user* back to the redirect url.
6. User can now access *protected API endpoints in the backend* as long as cookie is not deleted or expires (assuming frontend + backend are in the **same domain**)
