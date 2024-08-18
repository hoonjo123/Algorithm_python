console.log(10);
console.log("I'm Iron man")
console.log("He said \"I'm Iron man\"");
console.log(`He said "I'm Iron man"`);

console.log('Hello'+'JavaScript');

console.log("한국 영화 역사상 아카데미상을 받은 것은 '기생충'이 처음이다.")
console.log(`인간은 사회적 동물이다.`);

//불대수

console.log(2 > 1);
console.log(2 < 1);

console.log(true && true);
console.log(true || false);

//typeof 연산자
console.log(typeof 101); 
//number 출력

//NaN ( Not a number ) - 문자열과 숫자값을 연산
console.log(typeof 8 - 3);
console.log(typeof ( 8 - 3 ));

//형변환 - falsy값
console.log('');
console.log(NaN);
console.log('false')

//템플릿 문자열
let number = 3;

function getTwice(x){
  return x * 2;
}

console.log(`${number}의 두 배는 ${getTwice(number)}입니다`)

//null, undefined
//null : 값이 없다. 의도적으로 표현할 때
//undefined : 값이 없다는걸 확인할 때

let codeit;
console.log(codeit);

// -> undefined가 나옴

/**할당 연산자
 * //오른쪽에 있는 p 연산자를 왼쪽에 있는 p연산자에 할당한다.
let name = 'hoon';
let x = 5;
x = x - 2;
console.log(x);

// 다음 두 줄은 같습니다
x = x + 1;
x += 1;

// 다음 두 줄은 같습니다
x = x + 2;
x += 2;

// 다음 두 줄은 같습니다
x = x * 2;
x *= 2;

// 다음 두 줄은 같습니다
x = x - 3;
x -= 3;

// 다음 두 줄은 같습니다
x = x / 2;
x /= 2;

// 다음 두 줄은 같습니다
x = x % 7;
x %= 7;
*/

//for in 문

let myInfo = {
  name: 'hoon',
  bornYear: '1994',
  isVeryNice: true,
  worstCourse: null,
  bestCourse: '자바스크립트'
}

for ( let k in myInfo){
  console.log(k);
  console.log(myInfo[k]);
}

let day = time / (1000 * 60 * 60 * 24);
let today = new Date(2112, 7, 24);
let jaeSangStart = new Date(2109, 6, 1);

function workDayCalc(startDate, endDate) {
	// 여기에 코드를 작성하세요
	let time = endDate - startDate;
	let day = time / (1000 * 60 * 60 * 24);
	console.log(`오늘은 입사한 지 ${day}일째 되는 날 입니다.`);
}

workDayCalc(jaeSangStart, today);

//Array
let courseRanking = [
  'basic course for javascript programming',
  'control of version with learing Git'
];

console.log(courseRanking[1]); //indexing ( start from '0' )
