import requests
import markdownify

# LeetCode GraphQL endpoint
GRAPHQL_URL = "https://leetcode.com/graphql/"

# GraphQL query to fetch a question by titleSlug
QUERY = """
#graphql
query selectProblem($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        boundTopicId
        title
        titleSlug
        content
        translatedTitle
        translatedContent
        isPaidOnly
        difficulty
        likes
        dislikes
        isLiked
        similarQuestions
        exampleTestcases
        contributors {
            username
            profileUrl
            avatarUrl
        }
        topicTags {
            name
            slug
            translatedName
        }
        companyTagStats
        codeSnippets {
            lang
            langSlug
            code
        }
        stats
        hints
        solution {
            id
            canSeeDetail
            paidOnly
            hasVideoSolution
            paidOnlyVideo
        }
        status
        sampleTestCase
        metaData
        judgerAvailable
        judgeType
        mysqlSchemas
        enableRunCode
        enableTestMode
        enableDebugger
        envInfo
        libraryUrl
        adminUrl
        challengeQuestion {
            id
            date
            incompleteChallengeCount
            streakCount
            type
        }
        note
    }
}
"""


def fetch_leetcode_question(title_slug):
    try:
        # Send the GraphQL request
        response = requests.post(
            GRAPHQL_URL,
            json={"query": QUERY, "variables": {"titleSlug": title_slug}},
            headers={
                "Content-Type": "application/json",
                # Uncomment the next line if authentication is required
                # "Authorization": "Bearer YOUR_ACCESS_TOKEN"
            },
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Print the fetched data
        if "errors" in data:
            print("GraphQL Errors:", data["errors"])
        else:
            html = data["data"]["question"]["content"]
            file_path = "question.md"
            with open(file=file_path, mode="w", encoding="utf-8") as f:
                f.write(markdownify.markdownify(html, heading_style="ATX"))
            # question = data["data"]["question"]
            # print("Title:", question["title"])
            # print("Difficulty:", question["difficulty"])
            # print("Total Accepted:", question["stats"]["totalAccepted"])
            # print("Total Submitted:", question["stats"]["totalSubmitted"])
    except requests.exceptions.RequestException as e:
        print("Request error:", e)

