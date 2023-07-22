// chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//     var currentTab = tabs[0]; 
//     var currentURL = currentTab.url;
//     alert(currentURL)
//     console.log(currentURL)
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "http://localhost:5000/test-it-up", true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.onreadystatechange = function() {
//       if (xhr.readyState == 4 && xhr.status == 200) {
//         var response = JSON.parse(xhr.responseText);
//         var score = parseFloat(response.Rating).toFixed(2);
//         chrome.storage.local.set({score: score});
//       }
//     }
//     xhr.send(JSON.stringify(currentURL));
//   });
  