package None;

import java.util.List;
import lombok.*;






/**
  A container for all PID4Cat instances.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Container  {

  private List<PID4CatRecord> containsPids;

}