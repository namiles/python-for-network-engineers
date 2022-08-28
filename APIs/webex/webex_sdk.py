from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='NWFmZjM2Y2MtODA5ZC00NTkwLThiMjYtZmM5ZmNmMTFlZjUwMzQ2ZGYwYWMtNWRj_P0A1_262cf59f-1417-4dce-b04b-539e93368fe3')

'''
Organizations
'''
orgs = api.organizations.list()
for org in orgs:
    print(org)

'''
Team Info
'''
teams = api.teams.list() #return as team class objects, not JSON data
print(type(teams))
# for team in teams:
#     print(team)
#     if getattr(team, 'name') == 'Devnet Pupils': # getattr can be used to get details about the class object
#         teamId = team.id #can also use decimal notation
#         print(teamId)

'''
People
'''
print(api.people.me())
emails = [
    'nick@nickmiles.me'
]
api.people.create(emails=emails, displayName='Nick Test', firstName='Nick', lastName='Test') # only email is required
print(api.people.get(email='nick@nickmiles.me'))
 

'''
Teams
'''

'''
Roles
'''
# roles = api.roles.list() 
# for role in roles:
#     print(role)
