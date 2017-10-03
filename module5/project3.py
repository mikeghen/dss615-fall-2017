main()
  aleTeams = getAleTeams()
  sortTeams(aleTeams)

def getAleTeams()
  aleTeams = {}

  # for each line in the file:
    teamData = line.split(',') # "Baltimore,98,23"
    aleTeams[teamData[0]] = {'wins': int(teamData[1]), 'loses': int(teamData[2])}

  return aleTeams

def sortTeams(aleTeams):

  # while there are teams in the aleTeams
    max = 0
    maxTeamName = ''
    for (team, winsLoses) in aleTeams.getItems():
      # first time through: (team, winsLoses) == ('Baltimore', { 'wins': 98, 'loses': 12 })
      ratio = winsLoses['wins']/winsLoses['loses']
      if ratio > max:
        max = ratio
        maxTeamName = team
    # write the team's data to a file
    # remove the team from the aleData
    del aleTeams[maxTeamName]






# NOTE: for (key, value) in aleData.getItems():
{
  'Baltimore': {
    'wins': 98,
    'loses': 12
  },
  'Philadelphia': {
    'wins': 89,
    'loses': '23'
  }
}
# aleData.getItems() ==>
[['Baltimore', { 'wins': 98, 'loses': 12 }],
 ['Philadelphia', { 'wins': 89, 'loses': 23 }]]

# for (key, value) in aleData.getItems():
# (key, value) on first iteration ==>
#  key == 'Baltimore'
#  value == { 'wins': 98, 'loses': 12 }
