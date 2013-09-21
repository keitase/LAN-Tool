function grabSteamID(communityURL)
{
	$(document).ready(function() { 
    $.get(communityURL, function(raw){

        var matches = raw.match(/g_steamID = "([0-9]*)"/i);
        var steamID = matches[1];

        alert(steamID);

    }, "html");
}); 
}