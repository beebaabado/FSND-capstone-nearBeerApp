import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Testing mode
TESTING = False

# Connect to the database
# COMPLETED IMPLEMENT DATABASE URL and set other options for SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/nearbeer'
DATABASE_URI='postgresql://postgres@localhost:5432/nearbeer'
DATABASE_URI_TEST = 'postgresql://postgres@localhost:5432/nearbeer_test'
# Prevent warning concerning use of Flask-SQLAlchemy event system causing overhead in memory usage
SQLALCHEMY_TRACK_MODIFICATIONS = False

# For unit testing purposes 
TEST_BREWER_AUTH_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI5ODY4MTg2LCJleHAiOjE2Mjk5NTQ1ODYsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.Ya_Z4-JQzN6Qyb8qQDofonR-Lr1qknVYk7ADJZmQQPTNXAHvWHge0QyFtuTCMPQMYiBju-U6xyC74cZvtUnIeOaWwqB1C1PPNUmsC-COsHYi5jai8hRmmVftyK7wXCklkA3sdpho0Tre_FFeVNh4JtCgwu-DX6ZSzkhZQ92sqbrz6B-G1BVJnWdX697_y0QuVOXpiiGmXzFQmOnIKw_JppzhgAEgOO6OGSuc2b9XntJvNCEhfog3Fq5fmdCW-FyEsoo_-3I24PMtruQ5VmGaO1nKeltJhxMkLI08lYxIa4hUbyygbdny5LiWLhz8YDoRA-u8l-LjIBRP1vzOxvPrqg'
TEST_BEER_LOVER_AUTH_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NTFjYTg1MjJhMDA2OTEyODhkYyIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI5NzU5OTU2LCJleHAiOjE2Mjk4NDYzNTYsImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJwYXRjaDpiZWVyLXVzZXItcmF0aW5nIl19.iFRcYlAmirdZd5_OXwSexRe3utG2DYW3tUVFre9H4MKW_kM8aO4Ddf4-oOrdCyMSqkfBmhbI1oDRkeXR1DH33h8rfskLEcBhy460L5joAi8e1w7ujWZ28Inzq-E5jZYieBwoLR44d2UN0z6OvwclQTZ9CzRgiNI9vYRpe7NtNNZcfV91YTOvgjeA9EK7axjjPbxlHPsjemIvu7JP_BaTJ6Faq9B0Fhvj5ZTAuAn9dCOQ2ZdoVi3efoCx9WzAQ08VKjPqHR23TgQlI7HGG6UbAWa4EgOVBJFfztvl7-Yqc9eHQFA-Kgrk3Vmqkesg1ax4Rv9kpPwEOh3VQ_UL0x5fLQ'
TEST_INVALID_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldIdHhPZnhSeUZTYWw1TTJjN2lPeSJ9.eyJpc3MiOiJodHRwczovL3Byb2R1Y3QtZGVtb3MudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZTg4NWJlNTMwODA5MDA2OGZmZjU0MiIsImF1ZCI6WyJiZWVybmVhciIsImh0dHBzOi8vcHJvZHVjdC1kZW1vcy51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjI2MzYwNTM5LCJleHAiOjE2MjYzNjc3MzksImF6cCI6InppUjNDdXczU1dtRmhrUFdmVGhGOUxEejdna1huTUg2Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpiZWVycyIsImdldDpiZWVyLWRldGFpbHMiLCJnZXQ6YmVlcnMiLCJnZXQ6c3R5bGVzIiwicGF0Y2g6YmVlci11c2VyLXJhdGluZyIsInBvc3Q6YmVlcnMiLCJ2aWV3OnNpbXBsZSJdfQ.qt7Xv8TyJKoqqx-izkMnylx_KVTn9XLVCsET5RmmVQyJs_4yg_wiwpqqwh5W7nxkBUd6tHzMCd3vfrBwOm3Xfdn7iGYqTsBjpSsusuCo0vWlsiCiX73EZi6X6t70lmvEvyZ2L81NVUfBpMc1Yhmo_w9i9srpgys-wZj-QY5Fo77Vsx4Nih5zGR8bTgbWIWBmI1odYmoATTJfNNP3iwlbbigpnAbViU316PI5MFHCaSBWp3Q9NL_Tb6Qd1j41ezj3kPqF0TlGuPo-Lpz1BOxcbDboFnzei8g4nhfFzU1gSNeCUZdeEJViON_2VaVkV0HLaYeRL8xeaP54PUnbzNEySP'
