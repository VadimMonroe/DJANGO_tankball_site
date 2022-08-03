
let directory_root = "http://94.154.11.51/static/main/"
//let directory_root = "http://127.0.0.1:8081/static/main/";

const canvas = document.querySelector('canvas');

playGame();

function playGame() {
	var displayWidth = canvas.width = window.innerWidth;
	var displayHeight = canvas.height = Math.round(displayWidth - (displayWidth/100*40));

	var x = 50;
	var y = 50;

	var rightPressed = false;
	var leftPressed = false;
	var upPressed = false;
	var downPressed = false;

	var tumblr = true;

	class Tank{
	  constructor(x, y, color, angle) {
	    this.x = x;
	    this.y = y;

	    this.tank_width = 45.6 * 2;
	    this.tank_height = 72.7 * 2;

	    this.tank_color = color;

	    this.radians = Math.PI/180;
	    this.angle = angle;
	    this.rotate = this.radians * this.angle;
	    // var speed = new Vec2(1, 0);

	    this.img = new Image();

	    if (color === 'orange') {
		    this.img.src = directory_root + 'img/orange_tank.png';
	    } else if (color === 'blue') {
		    this.img.src = directory_root + 'img/blue_tank.png';
	    }

	    this.speed = 0;
  		this.rotateSpeed = 2;
  		this.acceleration = 0.1;

  		this.angleSign = 0;
  		this.speedSign = 0;

		this.pushX = 0;
	    this.pushY = 0;

	  }

	  tankMovement() {
		if (rightPressed) {
			this.angleSign = 1;
		} else if (leftPressed) {
			this.angleSign = -1;
		} else {
			this.angleSign = 0;
		}

		 if (upPressed) {
			this.speedSign = -1;
		} else if (downPressed) {
			this.speedSign = 1;
		} else {
			this.speedSign = 0;
			if (this.speed > 0) {
				this.speed -= 0.05;
			} else if (this.speed < 0) {
				this.speed += 0.05;
			} else {
				this.speed = 0;
			}
		}

		if (this.speed >= 2) {
			this.speed -= 0.1;
		} else if (this.speed <= -2) {
			this.speed += 0.1;
		} else {
	    	this.speed += this.speedSign * this.acceleration;
		}

		this.angle += this.angleSign * this.rotateSpeed;
		this.rotate = this.radians * this.angle;
		}

		render(){
			// ctx.clearRect(0,0,this.tank_width,this.tank_height);

			// ctx.save();
			// ctx.clearRect(this.x-10 - this.tank_width/2, 
			// 	this.y-10 - this.tank_height/2, 
			// 	this.tank_width+20, 
			// 	this.tank_height+10);
			// ctx.translate(this.x, this.y);
			// ctx.rotate(this.rotate);
			// ctx.drawImage(this.img, -(this.tank_width/2), -(this.tank_height/2), this.tank_width, this.tank_height);
			// ctx.restore();

			
			ctx.save();
			ctx.beginPath();
			ctx.translate(this.x, this.y);
			ctx.rotate(this.radians * (this.angle - 90));
			ctx.drawImage(this.img, -(this.tank_width/2), -(this.tank_height/2), this.tank_width, this.tank_height);
			ctx.closePath();
			ctx.restore();
			
			}

		move() {
		    // if(this.x <= 0 || this.x >= displayWidth - this.width || this.y <= 0 || this.y >= displayHeight - this.height) {
		      
		    //   this.speed = 0;

		    //   this.pushX = this.x > this.width/2 ? -1 : 1;
	      	//   this.pushY = this.y > this.height/2 ? -1 : 1;
		    // }

		    this.x += Math.cos(this.rotate) * this.speed + this.pushX;
		    this.y += Math.sin(this.rotate) * this.speed + this.pushY;

		    this.render();
		}

		draw() {
			this.tankMovement();
			this.move();
			}
		}

	class Ball {
	  constructor() {
	    this.x = displayWidth / 2;
	    this.y = displayHeight / 2;

	    this.ball_radius = 40;
	    this.ball_width = 100;
	    this.ball_height = 100;

	    this.img = new Image();
	    this.img.src = directory_root + 'img/ball.png';
	    // this.img.scale = -100;
	  }

	  draw() {
	  	// ctx.fillRect(this.x, this.y, this.ball_width, this.ball_height);

	  	// ctx.beginPath();
	  	// ctx.fillStyle = 'red';
	  	// ctx.strokeStyle = 'black';
	  	// ctx.arc(this.x, this.y, this.ball_radius, 0, Math.PI*2);
	  	// ctx.fill();
	  	// ctx.stroke();

	  	ctx.drawImage(this.img, 
			this.x-this.ball_width/2, 
			this.y-this.ball_height/2, 
			this.ball_width, 
			this.ball_height);
	  }
	}


	// function firstStaticFunc() {
	// 	ctx.strokeRect(x, y, 100, 100);
	// }

	function textPrint(color='white', font="50px Arial", text='text', x=20, y=50) {
		ctx.beginPath();
		ctx.fillStyle = color;
		ctx.font = font;
		ctx.fillText(text, x, y);
		ctx.closePath();
	}


	function movementListener() {
	    document.addEventListener("keydown", keyDownHandler, false);
	    document.addEventListener("keyup", keyUpHandler, false);
	    // document.addEventListener("mousemove", mouseMoveHandler, false);

	    function keyDownHandler(e) {
	        if(e.code  == "ArrowRight") // 39 right
	            rightPressed = true;
	        else if(e.code == 'ArrowLeft') // 37 left
	            leftPressed = true;
	        else if(e.keyCode == 38) // 38 up
	            upPressed = true;
	        else if(e.keyCode == 40)// 40 down
	        	downPressed = true;
	    }
	    function keyUpHandler(e) {
	        if(e.code == 'ArrowRight') {
	            rightPressed = false;
	        } else if(e.code == 'ArrowLeft') {
	            leftPressed = false;
	        } else if(e.keyCode == 38) {
	            upPressed = false;
	        } else if(e.keyCode == 40) {
	            downPressed = false;
	        }
	    }
	}

	function loop() {
		ctx.clearRect(0, 0, displayWidth, displayHeight);

		textPrint();

		movementListener();
		// document.onkeypress = changeMotion;


		ball.draw();
		orange_right_tank.draw();
		blue_left_tank.draw();

		// setTimeout(loop, 15);
		// setInterval(loop, 100);
		requestAnimationFrame(loop);
	}

	let ball = new Ball();
	let orange_right_tank = new Tank(displayWidth*0.75, displayHeight*0.75, 'orange', 0);
	let blue_left_tank = new Tank(displayWidth*0.25, displayHeight*0.25, 'blue', 180);


	if (canvas.getContext){
	 	var ctx = canvas.getContext('2d');
		loop();
	}
}