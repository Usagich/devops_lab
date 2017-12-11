import getpass
import git
import time
import datetime
import requests
import argparse

###Put this script in your local git repo path

class PRstat():
    def __init__(self, username, password, repo, branch):
        self.__username = username
        self.__password = password
        self.__repo = repo
        self.__branch = branch
        self.__jsonForAllURL = repo.json()
        while "next" in repo.links.keys():
            nextPull = repo.links["next"]["url"]
            repo = requests.get(nextPull, auth=(username, password))
            self.__jsonForAllURL = self.__jsonForAllURL + repo.json()

    ##without JSON

    ##what time it was when last commited
    def getHourOfCommit(self):
        return (self.__branch.commit.authored_datetime.hour)

    ##how many hours passed since last commited
    def getHourSinceCommit(self):
        return ((time.time() - self.__branch.commit.authored_datetime.timestamp()) / 60 / 60)

    ##what day of the month it was when
    def getDayOfCommit(self):
        return (self.__branch.commit.authored_datetime.day)

    ##how many days passed since was commited
    def getDaysSinceCommit(self):
        return ((time.time() - self.__branch.commit.authored_datetime.timestamp()) / 60 / 60 / 24)

    ##how many weeks passed since was commited
    def getWeekSinceCommit(self):
        return ((time.time() - self.__branch.commit.authored_datetime.timestamp()) / 60 / 60 / 24 / 7)

    ##commitID - version
    def getInstalledVersion(self):
        return str(self.__branch.commit.hexsha)

    ##Latest commit author name:
    def getCommiterName(self):
        return str(self.__branch.commit.author.name)

    ##day of the week opened
    def getWeekDayCommit(self):
        return self.__branch.authored_datetime.ctime()[0:3]

    ####with JSON

    ##number of pulls
    def getOverallNumberOfPulls(self):
        return int(self.__repo.json()[0]["number"])

    ##merged/closed
    def getPullsTypeNumbers(self):
        __closedPull = 0
        __mergedPull = 0

        for i in range(self.getOverallNumberOfPulls()):
            if self.__jsonForAllURL[i]["state"] == "closed":
                __closedPull += 1
            elif self.__jsonForAllURL[i]["merged_at"]:
                __mergedPull += 1
        return (__closedPull, __mergedPull)

    ##pulls before/after date
    def getPullsByDay(self):
        for i in range(self.getOverallNumberOfPulls()):
            if self.__jsonForAllURL[i]["state"] == "open":
                openDay = (self.__jsonForAllURL[i]["created_at"].split("T")[0]).split("-")
                openDay = datetime.date(int(openDay[0]), int(openDay[1]), int(openDay[2]))
                if openDay == datetime.date.today():
                    print(("Request number " + str(self.__jsonForAllURL[i]["number"]) + " was opened today"))
                else:
                    diffd = str(datetime.date.today() - openDay).split()[0]
                    print(("Request number " + str(self.__jsonForAllURL[i]["number"]) + " was opened {} day(s) ago").format(diffd))

    ##get closing date
    def getClosedDate(self):
        for i in range(self.getOverallNumberOfPulls()):
            if self.__jsonForAllURL[i]["state"] == "closed":
                dateClosed = (self.__jsonForAllURL[i]["closed_at"].split("T")[0]).split("-")
                print((str(self.__jsonForAllURL[i]["number"]) + " request was closed: " + "{}").format(dateClosed))

    ##get lines info
    def getLinesNumber(self):
        for i in range(self.getOverallNumberOfPulls()):
            eachURL = self.__jsonForAllURL[i]["url"]
            count = requests.get(eachURL, auth=(self.__username, self.__password))
            print(str(self.__jsonForAllURL[i]["number"]) + " request INFO:")
            if count.json()["deletions"]:
                print(str(count.json()["deletions"]) + " lines deleted")
            else:
                print("0 lines deleted")
            if count.json()["additions"]:
                print(str(count.json()["additions"]) + " lines added")
            else:
                print("0 lines added")

    ##comments info
    def getCommentsNumber(self):
        for i in range(self.getOverallNumberOfPulls()):
            eachURL = self.__jsonForAllURL[i]["url"]
            comcount = requests.get(eachURL, auth=(self.__username, self.__password))
            if comcount.json()["review_comments"]:
                print(str(self.__jsonForAllURL[i]["number"]) + "th request commented " + str(comcount.json()["review_comments"])+ " times")
            else:
                print(str(self.__jsonForAllURL[i]["number"]) + "th request commented 0 times")

####console input


parser = argparse.ArgumentParser()
parser.add_argument('-ut', '--usertarget', required=True, default='alenaPy', help='github.com repository owner, mandatory paramether')
parser.add_argument('-us', '--userself', action='store_true', help='Your github.com user')
parser.add_argument('-r', '--repo', required=True, default='devops_lab', help='github.com repository, mandatory paramether')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-id', '--idcommit', action='store_true', help='Get last commit ID (version)')
parser.add_argument('-hoc', '--hourofcommit', action='store_true', help='What time it was when last commited')
parser.add_argument('-hsc', '--hoursincecommit', action='store_true', help='How many hours passed since last commited')
parser.add_argument('-doc', '--dayofcommit', action='store_true', help='What day of the month it was when')
parser.add_argument('-dsc', '--daysincecommit', action='store_true', help='How many days passed since repo was commited')
parser.add_argument('-wsc', '--weeksincecommit', action='store_true', help='How many weeks passed since repo was commited')
parser.add_argument('-woc', '--weekofcommit', action='store_true', help='Day of the week opened')
parser.add_argument('-an', '--autorname', action='store_true', help='Latest commit author name')
parser.add_argument('-np', '--numberpulls', action='store_true', help='Number of pulls')
parser.add_argument('-mc', '--mergedclosed', action='store_true', help='Merged/closed pulls')
parser.add_argument('-ba', '--beforeaftertoday', action='store_true', help='Pulls before/after current date')
parser.add_argument('-cl', '--closeday', action='store_true', help='Get closing date')
parser.add_argument('-li', '--linesinfo', action='store_true', help='Get lines info')
parser.add_argument('-com', '--comments', action='store_true', help='Comments info')


args = parser.parse_args()

userTarget = str(args.usertarget)
userSelf = str(args.userself)
repoName = str(args.repo)

url = "https://api.github.com/repos/" + userTarget + "/" + repoName + "/pulls?state=all"
repoLocal = git.Repo(repoName)
password = getpass.getpass()
branch = repoLocal.head.reference
repoGlobal = requests.get(url, auth=(userSelf, password))


print("#####here#####is#####your#####info#####")

statObject = PRstat(userSelf, password, repoGlobal, branch)

#if args.version:
#    print("Version", str(args.version))

if args.idcommit:
    print("Commit ID is", statObject.getInstalledVersion())

if args.hourofcommit:
    print("Committed at:", statObject.getHourOfCommit())

if args.hoursincecommit:
    print("Since committed passed", statObject.getHourSinceCommit(), "hours")

if args.dayofcommit:
    print("Committed at:", statObject.getDayOfCommit())

if args.daysincecommit:
    print("Since committed passed", statObject.getDaysSinceCommit(), "days")

if args.weeksincecommit:
    print("Since committed passed", statObject.getWeekSinceCommit(), "weeks")

if args.weekofcommit:
    print("Committed at:", statObject.getWeekDayCommit())

if args.autorname:
    print("Latest commit author name is", statObject.getCommiterName())

if args.numberpulls:
    print("Number of pull requests is", statObject.getOverallNumberOfPulls())

if args.mergedclosed:
    print("Number of merged, closed pull requests is", statObject.getPullsTypeNumbers())

if args.beforeaftertoday:
    statObject.getPullsTypeNumbers()

if args.closeday:
    statObject.getClosedDate()

if args.linesinfo:
    statObject.getLinesNumber()

if args.comments:
    statObject.getCommentsNumber()





