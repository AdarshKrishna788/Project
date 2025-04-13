// import { Component } from '@angular/core';
// import { AuthService } from '../../core/services/auth.service';
// import { User } from '../../core/models/user.model';
// import { CommonModule } from '@angular/common';
// import { ActivatedRoute, Router } from '@angular/router';

// @Component({
//   selector: 'app-profile',
//   standalone: true,
//   imports: [CommonModule],
//   template: `
//     <div class="container" *ngIf="user">
//       <h2>Welcome, {{ user.username }}</h2>
//       <img [src]="user.profilePic" alt="Profile Picture" class="profile-pic" />
//       <button (click)="logout()">Logout</button>
//     </div>
//   `,
//   styles: [
//     `
//       .container {
//         max-width: 400px;
//         margin: 2rem auto;
//         padding: 2rem;
//         border: 1px solid #ccc;
//         border-radius: 8px;
//         text-align: center;
//       }
//       .profile-pic {
//         width: 100px;
//         height: 100px;
//         border-radius: 50%;
//         object-fit: cover;
//         margin-bottom: 1rem;
//       }
//       button {
//         padding: 10px;
//         background-color: #f44336;
//         color: white;
//         border: none;
//         border-radius: 4px;
//         cursor: pointer;
//       }
//     `
//   ]
// })
// export class ProfileComponent {
//   user: User | null;

//   constructor(private authService: AuthService,private router:Router) {
//     this.user = this.authService.getCurrentUser();
//   }

//   logout() {
//     this.authService.logout();
//     this.router.navigateByUrl('login');

//   }
// }


import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient} from '@angular/common/http';
import { AuthService } from '../../core/services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'] 
})
export class ProfileComponent {

  response: any;

  formData: { [key: string]: number } = {
    "Time interval between two consecutive R waves(RR interval)": 206.0,
    "Time between the end of one QRS complex and the beginning of the next": 243.0,
    "PPeak": 0.047969956,
    "TPeak": 1.541606797,
    "RPeak": 1.509806577,
    "SPeak": 1.509806577,
    "QPeak": 0.011090966,
    "Qrs_interval": 9,
    "Pq_interval": 3,
    "Qt_interval": 13,
    "St_interval": 1,
    "negative deflection (Q wave), a larger, positive deflection (R wave), negative deflection (S wave)": 0.011090966,
    "Qrs_morph1": 0.013109427,
    "Qrs_morph2": 0.167740782,
    "Qrs_morph3": 0.583400545,
    "Qrs_morph4": 1.119587456,
    "pre-RR": 206.0,
    "post-RR": 243.0,
    "pPeak": -0.034179402,
    "tPeak": 0.296782222,
    "rPeak": 0.064287214,
    "sPeak": -0.57742044,
    "qPeak": -0.038414812,
    "qrs_interval": 34,
    "pq_interval": 8,
    "qt_interval": 49,
    "st_interval": 7,
    "qrs_morph0": -0.038414812,
    "qrs_morph1": -0.033358336,
    "qrs_morph2": -0.028278429,
    "qrs_morph3": -0.024205756,
    "qrs_morph4": 0.05058648
  };

  keys: string[] = Object.keys(this.formData);
  message: string = '';

  constructor(private http: HttpClient, private authService:AuthService, private router:Router) {}

  // Increment value
  increment(key: string) {
    if (typeof this.formData[key] === 'number') {
      this.formData[key]++;
    }
  }

  // Decrement value
  decrement(key: string) {
    if (typeof this.formData[key] === 'number') {
      this.formData[key]--;
    }
  }

  // Submit data to backend
  onSubmit() {
    this.authService.getModelResponse(this.formData).subscribe({
      next: (response) => {
        console.log(response)
        this.response=response
        this.message = `Response: ${JSON.stringify(response)}`;
        console.log(this.message)
      },
      error: (error) => {
        this.message = `Error: ${error.message}`;
      }
    });
  }




  logout() {
        this.authService.logout();
        this.router.navigateByUrl('login');
      }
}
