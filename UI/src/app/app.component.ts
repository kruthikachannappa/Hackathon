import {ChangeDetectorRef, Component} from '@angular/core';
import {FormsModule, FormGroup, FormBuilder, Validators} from '@angular/forms';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  show = false;
  button = false;
  showScore = false;
  tn = '30%';
  fp = '20%';
  tp = '10%';
  title = 'Hackathon';
  pdfSrc: string = '/pdf-test.pdf';
  formGroup = this.formbuilder.group({
    file: [null, Validators.required]
  });
  private contents: any;
  core = ['utilizes recurrent layers', 'rich joint embedding', 'tasks requiring sequential',
    'single model outperforms', 'level function learns', 'learning goal', 'major challenge', 'primary difficulty'];
  peripherial = [ 'visual system', 'based segmentation', 'extensive evidence', 'paper presents',
    'intuitive approach', 'obtain segments', 'convolutional network', 'segment objects', 'single frame'];
  other = ['obtain segments', 'convolutional network', 'segment objects', 'single frame', 'key role',
    'straightforward approach', 'cleverly designed' ]
  constructor(private formbuilder: FormBuilder, private cd: ChangeDetectorRef) {}
  onFileChange(event) {
    let reader = new FileReader();
    if(event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);

      reader.onload = () => {
        this.formGroup.patchValue({
          file: reader.result
        });
        this.cd.markForCheck();
      };
    }
  }
  onSubmit(){
    console.log(this.formGroup);
    this.show = true;
    this.button = true;
  }
  score(){
    this.showScore = true;
    this.tn = '10%';
    this.fp = '20%';
    this.tp = '30%';
  }
}
