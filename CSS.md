# CSS

## Common CSS Expansions

Made by [twitter] @dustinknopoff

### Full Screen Background

Description:

> Creates a full screen background.

` fullbg ../assets/bg.jpg`

will render:


```css
 html {
     background: url("../assets/bg.jpg") no-repeat center center fixed;
     -webkit-background-size: cover;
     -moz-background-size: cover;
     -o-background-size: cover;
     background-size: cover;
     width: 100%;
     height: 100%;
 
 }
 
 ```

Languages: ['css']



### Media Query

Description:

> Creates media query.

` mq 768`

will render:


```css
 @media only screen and (max-width: 768px) {
     
 }```

Languages: ['css']



