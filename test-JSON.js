function change(){
  const my_JSON = '{"g":"f", "a":"b"}';
  const parsed = JSON.parse(my_JSON);
  document.getElementById("hello").innerHTML = parsed["g"];
  document.getElementById("p1").innerHTML = parsed["a"];
}
