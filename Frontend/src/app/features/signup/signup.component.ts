// import { Component } from '@angular/core';
// import { FormBuilder, FormGroup, Validators } from '@angular/forms';
// import { Router } from '@angular/router';
// import { AuthService } from '../../core/services/auth.service';

// @Component({
//   selector: 'app-signup',
//   templateUrl: './signup.component.html'
// })
// export class SignupComponent {
//   signupForm: FormGroup;

//   constructor(
//     private fb: FormBuilder,
//     private authService: AuthService,
//     private router: Router
//   ) {
//     this.signupForm = this.fb.group({
//       fullname: ['', Validators.required],
//       username: ['', Validators.required],
//       password: ['', Validators.required],
//       confirmPassword: ['', Validators.required],
//       address: ['', Validators.required]
//     });
//   }

//   onSubmit() {
//     if (this.signupForm.valid) {
//       this.authService.signup(this.signupForm.value).subscribe(() => {
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
  selector: 'app-signup',
  standalone: true,
  imports: [FormsModule, CommonModule],
  template: `
    <div class="container">
      <h2>Sign Up</h2>
      <form (ngSubmit)="onSubmit()">
        <input type="text" [(ngModel)]="signupData.fullname" name="fullname" placeholder="Fullname" required />
        <input type="text" [(ngModel)]="signupData.username" name="username" placeholder="Username" required />
        <input type="password" [(ngModel)]="signupData.password" name="password" placeholder="Password" required />
        <input type="password" [(ngModel)]="signupData.confirmPassword" name="confirmPassword" placeholder="Confirm Password" required />
        <input type="text" [(ngModel)]="signupData.address" name="address" placeholder="Address" required />
        
        <!-- Gender field -->
        <select [(ngModel)]="signupData.gender" name="gender" required>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>

        <button type="submit">Sign Up</button>
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
      input, select, button {
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
export class SignupComponent {
  signupData = {
    fullname: '',
    username: '',
    password: '',
    confirmPassword: '',
    address: '',
    gender: 'male' 
  };

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  onSubmit() {
    if (this.signupData.password !== this.signupData.confirmPassword) {
      alert('Passwords do not match!');
      return;
    }

    this.authService.signup(this.signupData).subscribe(
      {
        next:(res)=>{
             console.log("received data",res);
             this.router.navigate(['/profile']);
        },
        error:(err)=>{console.log("signup error",err)}
      }
    );
  }
}
