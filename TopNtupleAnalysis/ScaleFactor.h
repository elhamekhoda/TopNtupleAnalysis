#ifndef SCALEFACTOR_H
#define SCALEFACTOR_H


    struct ScaleFactor {
        double nominal;
        double up;
        double down;
        
        ScaleFactor():
            nominal(1.),
            up(1.),
            down(1.)
        {};
    };


#endif //SCALEFACTOR_H
