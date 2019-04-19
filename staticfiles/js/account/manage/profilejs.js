

function showIssueCreated() {
    document.getElementById("issue-created-by-me-div").style.display = 'block';
    document.getElementById("issue-progressing-div").style.display = 'none';
    document.getElementById("issue-solved-div").style.display = 'none';

    document.getElementById("issues-created-by-me").classList.add("list-group-item-info");
    document.getElementById("issues-progressing").classList.remove("list-group-item-info");
    document.getElementById("solved-issues").classList.remove("list-group-item-info")

}

function showIssueProgressing() {
    document.getElementById("issue-created-by-me-div").style.display = 'none';
    document.getElementById("issue-progressing-div").style.display = 'block';
    document.getElementById("issue-solved-div").style.display = 'none';

    document.getElementById("issues-progressing").classList.add("list-group-item-info");
    document.getElementById("issues-created-by-me").classList.remove("list-group-item-info");
    document.getElementById("solved-issues").classList.remove("list-group-item-info")
}

function showSolvedIssues(){
    document.getElementById("issue-created-by-me-div").style.display = 'none';
    document.getElementById("issue-progressing-div").style.display = 'none';
    document.getElementById("issue-solved-div").style.display = 'block';

    document.getElementById("solved-issues").classList.add("list-group-item-info");
    document.getElementById("issues-created-by-me").classList.remove("list-group-item-info");
    document.getElementById("issues-progressing").classList.remove("list-group-item-info");
}