program heat2D
  use omp_lib
  implicit none
  real(8), allocatable, dimension(:,:) :: T, Tn, x, y
  real(8), allocatable, dimension(:,:) :: rhs, Told
  real(8) :: dx, dy, dt
  real(8) :: length
  real(8) :: alpha, beta
  real(8), parameter :: pi = 4.0*atan(1.0)
  integer :: i, j, imax, jmax, iter, itermax, inner, istep
  integer:: nthreads
  integer :: icenter, jcenter
  
  
  print *, "Enter imax and jmax"
  read *, imax, jmax
  print*, "Enter number of threads , machine default=", omp_get_max_threads()
  read*, nthreads

  call omp_set_num_threads(nthreads)
!  print*, "Testing openmp threads"
!  !$omp parallel
!  print*, "Hello OpenMP! from thread ", omp_get_thread_num()
!  !$omp end parallel
  
  length = 1.0
  dx = length / (imax-1)
  dy = length / (jmax-1)
  icenter = (imax/2) + 1
  jcenter = (jmax/2) + 1
  
  print*, "Enter dt ratio wrt  dx*dx =", dx*dx, " as reference."
  read*, dt
  print*, "Maximum iteration?"
  read*, itermax
  print*, "Steps for record"
  read*, istep

dt = dt*dx*dx

  allocate(T(imax,jmax), Tn(imax,jmax), x(imax,jmax), y(imax,jmax))
  allocate(rhs(imax,jmax), Told(imax,jmax) )
  
  !$omp parallel do private(i,j)
  do j = 1, jmax
     do i = 1, imax
        x(i,j) = (i-1)*dx
        y(i,j) = (j-1)*dx
     end do
  end do
  !$omp end parallel do

  !Intrinsic vectorization
  T = sin(pi*x)*sin(pi*y)
  Tn = T
  rhs = T
  Told = T

  !Dirichlet BC

  alpha = dt/(dx*dx)
  beta = dt/(dy*dy)

  open(2,file="peak.csv")
  rewind(2)
  write(2,*) "t, T_peak"
  
  !Time loop
  do iter = 0, itermax, istep


     do inner = 0, istep

        !$omp parallel do private(i,j)
        do j = 2, jmax-1
           do i = 2, imax-1

              rhs(i,j) = alpha*( T(i-1,j) - 2.0*T(i,j) + T(i+1,j) ) &
                   & +  beta*( T(i,j-1) - 2.0*T(i,j) + T(i,j+1) )
                      
           end do
        end do
        !$omp end parallel do
        
        !update
        !vectorization works better for updating the value
        Tn = T + rhs

        !For convergence calculation
        !Vectorization works better for copy too
        Told = T

        !For the next inner iteration
        T = Tn
     end do

     print*, iter*dt, Told(icenter,jcenter), T(icenter,jcenter), Tn(icenter,jcenter)
     write(2, *) iter*dt,",", Tn(icenter,jcenter)
     
  end do

  close(2)
    
  !Write to file
  open(1, file ="test.csv")
  rewind(1)
  write(1,*) "x,y,z,T "
  do j = 1, jmax
     do i = 1, imax
        write(1, *) x(i,j),",",y(i,j),",",0.0,",",T(i,j)
     end do
  end do
  close(1)

  
  
    
end program heat2D
