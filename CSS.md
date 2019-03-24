# CSS

## Common CSS Expansions

Made by [@dustinknopoff](https://dustinknopoff.me)

### Included Expanders

- [Full Screen Background](#full-screen-background)
- [Media Query](#media-query)
- [var](#var)

### Full Screen Background

Description:

> Creates a full screen background.

` fullbg ../assets/bg.jpg`

will render:


```css
 html {
     background: url("../assets/bg.jpg") no-repeat center center fixed;
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
     
 }
```

Languages: ['css']



### var

Description:

` var text-color-default #efefef`

will render:


```css
 --text-color-default: #efefef;
```

Languages: ['css']



