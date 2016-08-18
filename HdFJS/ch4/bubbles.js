var scores = [60, 50, 60, 58, 54, 54,
              58, 50, 52, 54, 48, 69,
              34, 55, 51, 52, 44, 51,
              69, 64, 66, 55, 52, 61,
              46, 31, 57, 52, 44, 18,
              41, 53, 55, 61, 51, 44];
var sols = [0, 0];
for(i = 0; i < scores.length; i++) {
  console.log("Bubble solution #" + i + " score: " + scores[i]);
  if(scores[i] > scores[sols[0]]) {
    sols[1] = sols[0];
    sols[0] = i;
  }
}

console.log("Bubble tests: " + scores.length);
console.log("Highest bubble score: " + scores[sols[0]]);
console.log("Solutions with highest score: #" + scores[sols[0]] + ", #" + scores[sols[1]]);
