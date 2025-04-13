// import { Component } from '@angular/core';
// import { FormBuilder, FormGroup, Validators } from '@angular/forms';
// import { Router } from '@angular/router';
// import { AuthService } from '../../core/services/auth.service';

// @Component({
//   selector: 'app-login',
//   templateUrl: './login.component.html'
// })
// export class LoginComponent {
//   loginForm: FormGroup;

//   constructor(
//     private fb: FormBuilder,
//     private authService: AuthService,
//     private router: Router
//   ) {
//     this.loginForm = this.fb.group({
//       username: ['', Validators.required],
//       password: ['', Validators.required]
//     });
//   }

//   onSubmit() {
//     if (this.loginForm.valid) {
//       this.authService.login(this.loginForm.value).subscribe(() => {
//         this.router.navigate(['/profile']);
//       });
//     }
//   }
// }


import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule],
  template: `
    <div class="container">
      <h2>Login</h2>
      <form (ngSubmit)="onSubmit()">
        <input type="text" [(ngModel)]="loginData.username" name="username" placeholder="Username" required />
        <input type="password" [(ngModel)]="loginData.password" name="password" placeholder="Password" required />
        <button type="submit">Login</button>
       <button type="button" (click)="navigateToSignup()" class="signup-btn">Sign Up</button>
      </form>
    </div>
  `,
  styles: [
    `
      .container {
        max-width: 400px;
        margin: 2rem auto;
        padding: 2rem;
        border: 1px solid #ccc;
        border-radius: 8px;
      }
      input, button {
        width: 100%;
        padding: 8px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
      }
      button {
        background-color: #4caf50;
        color: white;
        cursor: pointer;
      }
      button:disabled {
        background-color: #ccc;
      }
    `
  ]
})
export class LoginComponent {
  loginData = {
    username: '',
    password: ''
  };

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  onSubmit() {
    this.authService.login(this.loginData).subscribe({
      next: (res) => {
        console.log("login response", res);
        localStorage.setItem('user', JSON.stringify(res));
        this.router.navigate(['/profile']);
      },
      error: (err) => {
        console.log("login error", err);
      }
    });
    
  }
  navigateToSignup() {
    this.router.navigate(['/signup']);
  }
}
