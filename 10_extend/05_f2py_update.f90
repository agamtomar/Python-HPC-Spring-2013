! fortran 90 update

subroutine f2py_update90(np, u, dx2, dy2)
    integer, intent(in) :: np
    double precision, intent(inout) :: u(0:np-1, 0:np-1)
    double precision, intent(in) :: dx2, dy2
!f2py intent(in) :: dx2, dy2
!f2py intent(in, out) :: u
!f2py intent(hide) :: np

    double precision :: dnr_inv
    
    dnr_inv = 0.5d0 / (dx2 + dy2)
    
    u(1:np-2, 1:np-2) = ((u(0:np-3, 1:np-2) + u(2:np-1, 1:np-2)) * dy2 + (u(1:np-2, 0:np-3) + u(1:np-2, 2:np-1)) * dx2) * dnr_inv
end subroutine f2py_update90                  