function solvetactic() {
  var PHPSESSID = 'fef05d15d0a6b45f55ff71eb18c50d39';
  const urls = {
    next: 'https://www.chess.com/callback/tactics/rated/next',
    submit: 'https://chess.com/callback/tactics/submitMoves',
  };
  fetch(urls.next, {
    method: 'GET',
    headers: {
      phpsessid: 'd53827cb2fc6a9a9d9ee6fb16baed647',
    },
  })
    .then(function (res) {
      return res.json();
    })
    .then(function (tactic) {
      console.log(tactic);
    })
    .catch(console.error);
}
solvetactic();
