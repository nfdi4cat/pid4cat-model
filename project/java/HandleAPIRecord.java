package None;

import java.util.List;
import lombok.*;






/**
  A class representing a handle record query response of the REST (json) API of a handle server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleAPIRecord  {

  private Integer responseCode;
  private String handle;
  private List<HandleRecord> values;

}
