let name1 = "MAuricio";
const name2 = "Mauricio";

console.log(name1.localeCompare(name2));
console.log(2 ** 3);
console.log(Math.pow(2, 3))
console.log(Math.sqrt(2))

let matrix = [[1], [9,9, 8], [3,5,6]]
console.log(name1, name2, 're', 'fa');

matrix[0][1] = 3;
matrix.forEach(element => console.log(element));

console.log('\n---------------------------------\n');


const Quicksort = (arr) => {

  console.log(arr);
  if (arr.length <= 1) return arr

  let izq = [];
  let der = [];
  let aux = [];
  let pivote = arr.pop();

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] <= pivote) izq.push(arr[i]);
    else der.push(arr[i]);
  }
  return aux.concat(Quicksort(izq), pivote, Quicksort(der))
};


const arr = [32, 54, 31,123, 2, 95, 3, 183, 231];
Quicksort(arr);

