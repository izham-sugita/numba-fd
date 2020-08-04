program heat2D
  use omp_lib
  implicit none
  real(8), allocatable, dimension(:,:) :: T, Tn, x, y
  real(8) :: dx, dy, dt
  real(8) :: length
  real(8), parameter :: pi = 4.0*atan(1.0)
  integer :: i, j, imax, jmax, iter, itermax

  print *, "Enter imax and jmax"
  read *, imax, jmax

  call omp_set_num_threads(6)
  print*, "Testing openmp threads"
  !$omp parallel
  print*, "Hello OpenMP! from thread ", omp_get_thread_num()
  !$omp end parallel
  
  length = 1.0
  dx = length / (imax-1)
  dy = length / (jmax-1)

  allocate(T(imax,jmax), Tn(imax,jmax), x(imax,jmax), y(imax,jmax))

  !$omp parallel do private(i,j)
  do j = 1, jmax
     do i = 1, imax
        x(i,j) = (i-1)*dx
        y(i,j) = (j-1)*dx
        T(i,j) = sin(pi*x(i,j))*sin(pi*y(i,j))
        Tn(i,j) = T(i,j)
     end do
  end do
  !$omp end parallel do
  

  
end program heat2D
